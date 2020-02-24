from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from blog.models import Post, Reply, Comment, User, Subscribe, Category, Likes, Dislikes
from .forms import CommentForm, ReplyForm, PostForm, CategoryForm
from django.shortcuts import render, get_object_or_404
# from Bloger.settings import MEDIA_ROOT

# Create your views here.
def home(request):
    # user = User.objects.get(id = num)
    cats = Category.objects.all()
    subs = Subscribe.objects.filter(subscriber_id = request.user).values_list('category_id', flat=True)
    # print(subs)
    # print(cats)
    checks = Check(cats, subs)
    context = { 'cats' : cats,
                'checks' : checks }
    return render(request,'blogviews/home.html',context)

def subscribe(request, category_id):
    try:
        cat = Category.objects.get(id = category_id)
        print("s")
        Subscribe.objects.create(subscriber_id = request.user, category_id = cat)
    finally:
        return HttpResponseRedirect('/blog/home')


def unsubscribe(request,category_id):
    try:
        cat = Category.objects.get(id = category_id)
        sub = Subscribe.objects.get(subscriber_id = request.user, category_id = cat)
        print("uns")
        sub.delete()
    finally:
        return HttpResponseRedirect('/blog/home')    

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blogviews/allPosts.html'

def post_list(request):
    template_name = 'blogviews/allPosts.html'
    posts = Post.objects.all()
    categories = Category.objects.all()

    # base_path = MEDIA_ROOT#ADD MEDIA_ROOT in settings.py

    # media = MEDIA_ROOT
    # for post in posts:
    #     # post.image = post.image.decode('utf-8')
    #     post.image = os.path.join(MEDIA_ROOT, b64decode(post.image))

    context = {'post_list': posts, 'categories': categories}

    # context = {'post_list': posts, 'media':base_path}

    return render(request, template_name, context)

def post_detail(request, slug):
    template_name = 'blogviews/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    replies = Reply.objects.all()
    if not request.user.is_anonymous:
        likes = Likes.objects.filter(post=post, liker=request.user)
        dislikes = Dislikes.objects.filter(post=post, disliker=request.user)
    reply_form = ReplyForm()
    new_comment = None
    url = '/blog/'+ slug

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(url)
        else:
            raise ValidationError(_('Invalid value'), code='invalid')
    else:
        comment_form = CommentForm()

    if not request.user.is_anonymous:
        return render(request, template_name, {'post': post,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form,
                                                'replies': replies,
                                                'reply_form': reply_form,
                                                'likes': likes,
                                                'dislikes': dislikes})
    else:
        return render(request, template_name, {'post': post,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form,
                                                'replies': replies,
                                                'reply_form': reply_form})

def comment_reply(request, commentId, slug):
    comment = get_object_or_404(Comment, id=commentId)
    print(comment)
    url = '/blog/'+ slug

    if request.method == 'POST':
        print (request.GET)
        reply_form = ReplyForm(data=request.POST)
        print (reply_form)
        if reply_form.is_valid():

            # Create Reply object but don't save to database yet
            reply = reply_form.save(commit=False)
            # Assign the current comment to the reply
            reply.comment = comment
            reply.name = request.user
            # Save the reply to the database
            reply.save()
        else:
            raise ValidationError(_('Invalid value'), code='invalid')
    else:
        reply_form = ReplyForm()

    return HttpResponseRedirect(url)

def addPost(request):
    if(request.method=='POST'):
        form = PostForm(request.POST,request.FILES)

        if(form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return HttpResponseRedirect('/blog/allPosts')
        else:
            raise ValidationError(_('Invalid value'), code='invalid')
    else:
        form=PostForm()

    return render(request,'blogviews/newPost.html',{'form':form})

def addCategory(request):
    if(request.method=='POST'):
        form = CategoryForm(request.POST)

        if(form.is_valid()):
            category = form.save(commit=False)
            category.creator = request.user
            category.save()
            return HttpResponseRedirect('/blog/newPost')
        else:
            raise ValidationError(_('Invalid value'), code='invalid')
    else:
        form=CategoryForm()

    return render(request,'blogviews/newCategory.html',{'form':form})

def category_posts(request, category_id):
    template_name = 'blogviews/category_posts.html'
    posts = Post.objects.filter(category_id=category_id)

    categories = Category.objects.all()

    context = {'post_list': posts, 'categories': categories}

    return render(request, template_name, context)

def increment_likes(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.likes = post.likes + 1
    like = Likes(liker=request.user, post=post)
    dislike = Dislikes.objects.filter(disliker=request.user, post=post)

    if dislike:
        dislike.delete()
        post.dislikes -= 1

    post.save()
    like.save()
    url = '/blog/'+ slug
    return HttpResponseRedirect(url)

def increment_dislikes(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.dislikes = post.dislikes + 1
    dislike = Dislikes(disliker=request.user, post=post)
    like = Likes.objects.filter(liker=request.user, post=post)

    if like:
        like.delete()
        post.likes -= 1

    post.save()
    dislike.save()
    if(post.dislikes == 10):
        post.delete()
        return HttpResponseRedirect('/blog/allPosts')
    
    url = '/blog/'+ slug
    return HttpResponseRedirect(url)

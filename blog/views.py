from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from blog.models import Post, Reply, Comment, User, Subscribe, Category, Likes, Dislikes,Tag,undesiredWord
from .forms import CommentForm, ReplyForm, PostForm, CategoryForm
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
# from Bloger.settings import MEDIA_ROOT
n = 2
# Create your views here.
def home(request):
    # user = User.objects.get(id = num)
    cats = Category.objects.all()
    posts = Post.objects.all()[n-2:n]

    if not request.user.is_anonymous:
        subs = Subscribe.objects.filter(subscriber_id = request.user).values_list('category_id', flat=True)
    else:
        subs = []
    tags = Tag.objects.all()
    # print(tags[0])
    # print(type(tags[0]))
    # print(posts)
    # adjustTags(tags)
    contents = ShortIntro(posts)
    posts = merge(posts, contents)
    # print(posts)
    checks = Check(cats, subs)

    # if not request.user.is_anonymous:
    context = { 'cats' : cats,
                'checks' : checks,
                'posts' : posts, 
                'tags' : tags,
                }

    return render(request,'blogviews/home.html',context)

def next(request):
    global n
    counter = (Post.objects.all()).count()
    if n < counter:
        n += 2
    return HttpResponseRedirect('/blog/home')

def previous(request):
    global n
    counter = (Post.objects.all()).count()
    if n >= counter:
        n -= 2
    return HttpResponseRedirect('/blog/home')

def subscribe(request, category_id):
    try:
        cat = Category.objects.get(id = category_id)
        Subscribe.objects.create(subscriber_id = request.user, category_id = cat)
    finally:
        return HttpResponseRedirect('/blog/home')


def unsubscribe(request,category_id):
    try:
        cat = Category.objects.get(id = category_id)
        sub = Subscribe.objects.get(subscriber_id = request.user, category_id = cat)
        sub.delete()
    finally:
        return HttpResponseRedirect('/blog/home')

# def search(request):
#     posts = Post.objects.filter(attribute = value).values_list(flat=True)
#     print(posts)
#     return HttpResponseRedirect('/blog/home')


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blogviews/allPosts.html'

def post_list(request):
    # template_name = 'blogviews/allPosts.html'
    # posts = []
    # categories = Category.objects.all()
    # tags = Tag.objects.all()
    template_name = 'blogviews/allPosts.html'
    posts=filterPost()#caal to filterWordsFunction
    categories = Category.objects.all()

    context = {'post_list': posts, 'categories': categories}

    return render(request, template_name, context)


def filterPost():# this function to fillter all posts
    posts = Post.objects.all()
    forbWords=undesiredWord.objects.values_list('word',flat=True)
    for x in posts:
        for word in forbWords:
            if(word in x.title.lower()):
                x.title=x.title.lower()
                x.title=x.title.replace(word,'*'*len(word))
            if(word in x.content.lower()):
                x.content=x.content.lower()
                x.content=x.content.replace(word,'*'*len(word))
    return posts

def post_detail(request, slug):
    template_name = 'blogviews/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    replies = Reply.objects.all()
    categories = Category.objects.all()
#start filterComment&&replies&&postdetails
    #values_list('word') -> this to covert the result to tupe 
    #values_list('word', flat=True) -> afetr add(flat=True) it conver to string  
    forbWords=undesiredWord.objects.values_list('word',flat=True)
    for word in forbWords:
        if(word in post.title.lower()):
            post.title=post.title.lower()
            post.title=post.title.replace(word,'*'*len(word))
        if(word in post.content.lower()):
            post.content=post.content.lower()
            post.content=post.content.replace(word,'*'*len(word))
    for x in comments:
        for word in forbWords:
            if(word in x.body.lower()):
                x.body=x.body.lower()
                x.body=x.body.replace(word,'*'*len(word))
#endfilterComment
    for x in replies:
        for word in forbWords:
            if(word in x.body.lower()):
                x.body=x.body.lower()
                x.body=x.body.replace(word,'*'*len(word))
#endfilterreplies
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
                                                'categories': categories,
                                                'likes': likes,
                                                'dislikes': dislikes})
    else:
        return render(request, template_name, {'post': post,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form,
                                                'categories': categories,
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
            category.category_creator = request.user
            category.save()
            return HttpResponseRedirect('/blog/newPost')
        else:
            raise ValidationError(_('Invalid value'), code='invalid')
    else:
        form=CategoryForm()

    return render(request,'blogviews/newCategory.html',{'form':form})

def category_posts(request, category_id):
    template_name = 'blogviews/category_posts.html'

    # posts = Post.objects.filter(category_id=category_id)

    # categories = Category.objects.all()

    # context = {'post_list': posts, 'categories': categories}

    # return render(request, template_name, context)

    try:
        categories = Category.objects.all()
        posts = Post.objects.filter(category_id=category_id)
        category = Category.objects.get(id=category_id)
        context = {'post_list': posts, 'categories': categories, 'category': category}
    except:
        context = {'categories': categories}
    finally:
        return render(request, template_name, context)

### ________ Helping Logic __________ ###
#check subscribe and unsubscribe
def Check(cats, subs):
    Checks = []
    for cat in cats:
        # print(cat)
        if cat.id in subs:
            check = cat.id
        else:
            check = -1
        Checks.append(check)
    # print(Checks)
    return Checks

#Forming a short Intro from post
def ShortIntro(posts):
    words_list = []
    for post in posts:
        words = ""
        for word in (post.content).split()[:20]:
            words += word
            words += " "
        words += "..."
        words_list.append(words)
    return (words_list)

def merge(list1, list2): 
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list

# def adjustTags(tags):
#     tgs = []
#     for tag in tags:
#         if tag[1] != None : 
#             tgs.append(tag) 
#     print(tgs)
#     return tgs

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

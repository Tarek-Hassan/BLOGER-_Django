from django.shortcuts import render
from django.views import generic
from blog.models import Post, Reply, Comment, User, Subscribe
from .forms import CommentForm, ReplyForm, PostForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


# Create your views here.
def home(request, num):
    user = User.objects.get(id = num)
    subs = Subscribe.objects.all()
    context = { 'user' : user,
                'subs': subs }
    return render(request,'blogviews/home.html',context)

def post_list(request):
    template_name = 'blogviews/allPosts.html'
    posts = Post.objects.all()

    context = {'post_list': posts}

    return render(request, template_name, context)

def post_detail(request, slug):
    template_name = 'blogviews/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    replies = Reply.objects.all()
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
        comment_form = CommentForm()

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
        form=PostForm()

    return render(request,'blogviews/newPost.html',{'form':form})

from django.shortcuts import render
from django.views import generic
from blog.models import Post, Reply, User, Subscribe
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# from Bloger.settings import MEDIA_ROOT

# Create your views here.
def home(request, num):
    user = User.objects.get(id = num)
    subs = Subscribe.objects.all()
    context = { 'user' : user,
                'subs': subs }
    return render(request,'blogviews/home.html',context)

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blogviews/allPosts.html'

def post_list(request):
    template_name = 'blogviews/allPosts.html'
    posts = Post.objects.all()
    # base_path = MEDIA_ROOT#ADD MEDIA_ROOT in settings.py

    # media = MEDIA_ROOT
    # for post in posts:
    #     # post.image = post.image.decode('utf-8')
    #     post.image = os.path.join(MEDIA_ROOT, b64decode(post.image))

    context = {'post_list': posts}

    # context = {'post_list': posts, 'media':base_path}

    return render(request, template_name, context)

def post_detail(request, slug):
    template_name = 'blogviews/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    replies = Reply.objects.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'replies': replies})

from django.shortcuts import render
from django.views import generic
from blog.models import Post
from Bloger.settings import MEDIA_ROOT

# Create your views here.
def home(request):
    return render(request,'blogviews/home.html')

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
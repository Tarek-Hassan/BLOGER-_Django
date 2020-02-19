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
    media = MEDIA_ROOT #ADD MEDIA_ROOT in settings.py

    context = {'post_list': posts, 'media':media}

    return render(request, template_name, context)
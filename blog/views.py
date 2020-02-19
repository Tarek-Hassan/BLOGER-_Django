from django.shortcuts import render
from django.views import generic
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'blogviews/home.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogviews/allPosts.html'
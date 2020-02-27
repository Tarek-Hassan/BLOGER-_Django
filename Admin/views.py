from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError


# Create your views here.

def home(request):
    return render(request, 'Admin_Views/home.html')

def showusers(request):
    all_users = User.objects.all()
    context = {'all_users': all_users}
    return render(request, 'Admin_Views/usersTable.html', context)


def showUser(request, num):
    us = get_object_or_404(User,id=num)
    context = {'us': us}
    return render(request, 'Admin_Views/userDetails.html', context)


def addUser(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/users')
    return render(request, 'Admin_Views/userForm.html', {'form': form})


def editUser(request, num):
    us = get_object_or_404(User,id=num)
    if request.method == "POST":
        form = UserForm(request.POST, instance=us)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/users')
    else:
        form = UserForm(instance=us)
    return render(request, 'Admin_Views/userForm.html', {'form': form})

# def addstaff(request, num):
#     us = get_object_or_404(User,id=num)
#     us.is_staff=True
#     if(us.is_active==False):
#         us.is_active=True
#     us.save()
#     return HttpResponseRedirect('/admin/users')
#
# def blockUser(request, num):
#     us = get_object_or_404(User,id=num)
#     us.is_active=not us.is_active
#     us.save()
#     return HttpResponseRedirect('/admin/users')
#
def deleteUser(request, num):
    us = get_object_or_404(User,id=num)
    us.delete()
    return HttpResponseRedirect('/admin/users')

# def showposts(request):
#     all_posts = Post.objects.all()
#     context = {'all_posts': all_posts}
#     return render(request, 'Admin_Views/postsTable.html', context)
#
#
# def showPost(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     replies = Reply.objects.all()
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, 'Admin_Views/postDetails.html', {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form,
#                                            'replies': replies})
#
# def addPost(request):
#
#     form = PostForm()
#     if request.method == "POST":
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             newform = form.save(commit=False)
#             newform.author = request.user
#             newform.save()
#             return HttpResponseRedirect('/admin/posts')
#     return render(request, 'Admin_Views/postForm.html', {'form': form})
#
#
# def editPost(request, slug):
#     po = get_object_or_404(Post, slug=slug)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=po)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/admin/posts')
#     else:
#         form = PostForm(instance=po)
#     return render(request, 'Admin_Views/postForm.html', {'form': form})
#
#
# def deletePost(request, slug):
#     po =get_object_or_404(Post, slug=slug)
#     po.delete()
#     return HttpResponseRedirect('/admin/posts')
#
#
# def showcategory(request):
#     all_categories = Category.objects.all()
#     context = {'all_categories': all_categories}
#     return render(request, 'Admin_Views/categoriesTable.html', context)
#
# def addcategory(request):
#     form = categoryForm()
#     if request.method == "POST":
#         form = categoryForm(request.POST)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.category_creator = request.user
#             category.save()
#             return HttpResponseRedirect('/admin/categories')
#     return render(request, 'Admin_Views/categoryForm.html', {'form': form})
#
# def editcategory(request, num):
#     ct = get_object_or_404(Category,id=num)
#     if request.method == "POST":
#         form = categoryForm(request.POST, instance=ct)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.category_creator = request.user
#             category.save()
#             return HttpResponseRedirect('/admin/categories')
#     else:
#         form = categoryForm(instance=ct)
#     return render(request, 'Admin_Views/categoryForm.html', {'form': form})
#
#
# def deletecategory(request, num):
#     ct = get_object_or_404(Category,id=num)
#     ct.delete()
#     return HttpResponseRedirect('/admin/categories')

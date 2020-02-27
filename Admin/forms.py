from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import *



# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('id','username','first_name','last_name','email','date_joined',)

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title','slug','content','image','category',)
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'body')
#
# class categoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ('category_name',)







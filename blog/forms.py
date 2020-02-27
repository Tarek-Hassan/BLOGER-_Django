from .models import Comment, Reply, Post, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': ''}

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)
        labels = {'body': ''}

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','category','image')
        widgets = {
            'content': forms.Textarea(attrs={
                'required': True, 
                'placeholder': 'Write your content ...',
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= ('category_name',)
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

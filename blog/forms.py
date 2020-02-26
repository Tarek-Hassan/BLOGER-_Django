from .models import Comment, Reply, Post, Category, Tag
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
        fields=('title','content','category','image', 'tags')
        widgets = {
            'content': forms.Textarea(attrs={
                'required': True, 
                'placeholder': 'Write your content ...'
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model= Tag
        fields= ('tag',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= ('category_name',)

class SearchForm(forms.Form):
    Attribute = forms.CharField(required=False)
    Value = forms.CharField(required=False)



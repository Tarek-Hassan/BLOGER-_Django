from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import *



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','date_joined',)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','category','image', 'tags')
        widgets = {
            'content': forms.Textarea(attrs={
                'required': True,
                'placeholder': 'Write your content ...',
                'class':'summernote',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model= Tag
        fields= ('tag',)
        widgets = {
            'tag' : forms.TextInput(),
        }
        
class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

class WordForm(forms.ModelForm):
    class Meta:
        model = undesiredWord
        fields = ('word',)






from rest_framework import serializers
from blog.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','first_name','last_name','email', )
        # add fields i wnat too sent
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','category_name')
        # add fields i wnat too sent
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'
        # add fields i wnat too sent
    #    image upload_to='images/', null=True

class PostSerializer(serializers.ModelSerializer):
    author=UserSerializer(required=False, read_only=True)
    category=CategorySerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)
    tags=TagSerializer(many=True, required=False, read_only=True)
    class Meta:
        model=Post
        fields=('id','author','category', 'tags','image','slug','title','content','likes','dislikes')
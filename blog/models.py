from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Subscribe(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} subscribe to {}'.format(self.subscriber_id, self.category_id)

    class Meta:
        unique_together = ["category_id", "subscriber_id"]


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=1)
    # image = models.ImageField(upload_to='img/', null=True)
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Reply(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Reply {} by {}'.format(self.body, self.name)


class Likes(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')


class Dislikes(models.Model):
    disliker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_dislikes')


class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag1 = models.SlugField(max_length=30, null=True, blank=True)
    tag2 = models.SlugField(max_length=30, null=True, blank=True)
    tag3 = models.SlugField(max_length=30, null=True, blank=True)
    tag4 = models.SlugField(max_length=30, null=True, blank=True)
    tag5 = models.SlugField(max_length=30, null=True, blank=True)

    def __str__(self):
        return "{} ,{} ,{} ,{}".format(self.tag1, self.tag2, self.tag3, self.tag4)

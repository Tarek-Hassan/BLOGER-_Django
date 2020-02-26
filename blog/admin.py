from django.contrib import admin
from blog.models import Post, Comment, Reply, Category, Subscribe, Likes, Dislikes, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on', 'image', 'category_id', 'get_tags')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'body')

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'comment', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'body')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_creator', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ['category_name']

class LikesAdmin(admin.ModelAdmin):
    list_display = ('liker', 'post')

class DislikesAdmin(admin.ModelAdmin):
    list_display = ('disliker', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(Dislikes, DislikesAdmin)
admin.site.register(Subscribe)
admin.site.register(Tag)

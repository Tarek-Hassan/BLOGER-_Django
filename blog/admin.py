from django.contrib import admin
from blog.models import Post, Comment, Reply, Category, Subscribe,Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on', 'image', 'category_id')
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

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag1', 'tag2', 'tag3', 'tag4', 'tag5')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subscribe)
admin.site.register(Tag, TagAdmin)
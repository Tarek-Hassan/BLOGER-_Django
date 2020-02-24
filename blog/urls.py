from django.urls import path
from blog import views

urlpatterns=[
    path('home/<num>', views.home),
    path('allPosts/<category_id>', views.category_posts, name='category_posts'), 
    path('allPosts', views.post_list),
    path('newPost', views.addPost),
    path('newCategory', views.addCategory),
    path('<slug>/', views.post_detail, name='post_detail'),
    path('<slug>/<commentId>/', views.comment_reply, name="comment_reply"),
    path('<slug>/like', views.increment_likes, name="increment_likes"),
    path('<slug>/dislike', views.increment_dislikes, name="increment_dislikes"),  
]
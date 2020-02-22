from django.urls import path
from blog import views
urlpatterns=[
    path('home/<num>', views.home),
    # path('allPosts', views.PostList.as_view()),
    path('allPosts', views.post_list),
    path('newPost', views.addPost),
    path('<slug>/', views.post_detail, name='post_detail'),
    path('<slug>/<commentId>/', views.comment_reply, name="comment_reply"),
]
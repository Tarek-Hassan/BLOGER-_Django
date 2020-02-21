from django.urls import path
from blog import views
urlpatterns=[
    path('home', views.home),
    # path('allPosts', views.PostList.as_view()),
    path('allPosts', views.post_list),
    path('<slug>/', views.post_detail, name='post_detail'),
    path('<slug>/<commentId>/', views.comment_reply, name="comment_reply"),
]
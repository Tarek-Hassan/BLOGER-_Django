from django.urls import path
from blog import views
urlpatterns=[
    path('home', views.home),
    # path('allPosts', views.PostList.as_view()),
    path('allPosts', views.post_list)
]
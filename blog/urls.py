from django.urls import path
from blog import views
urlpatterns=[
    path('home/<num>', views.home),
    # path('allPosts', views.PostList.as_view()),
    path('allPosts', views.post_list),
    # path('index', views.post_list),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
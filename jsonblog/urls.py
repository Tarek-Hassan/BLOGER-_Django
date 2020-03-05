from django.urls import path
from jsonblog import views

urlpatterns=[
    path('posts/', views.PostListCreateAPIView.as_view(), name='api-post-list'),
    path('posts/<pk>/', views.PostDetailsAPIView.as_view(), name='api-post-details'),
    path('User/', views.UserListCreateAPIView.as_view(), name='api-User-list'),
    path('User/<pk>/', views.UserDetailsAPIView.as_view(), name='api-User-details'),


    ]
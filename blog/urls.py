from django.urls import path
from blog import views

urlpatterns=[
    path('home/', views.home, name='home'),
    path('sub/<category_id>', views.subscribe, name ='subscribe'),
    path('unsub/<category_id>', views.unsubscribe, name ='unsubscribe'),
    path('next', views.next, name ='next'),
    path('previous', views.previous, name ='previous'),
    # path('search', views.search, name ='search'),
    path('cat/<category_id>', views.category_posts, name='category_posts'),
    # path('allPosts', views.PostList.as_view()),
    path('allPosts/<slug>', views.post_list, name='allPosts'),
    # path('index', views.post_list),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
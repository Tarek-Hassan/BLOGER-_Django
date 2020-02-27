from django.conf.urls import url
from django.urls import path
from Admin import views
app_name='Admin'

urlpatterns = [
    url(r'^$', views.home),
    path('users', views.showusers),
    path('show_user/<num>', views.showUser),
    path('add_user', views.addUser),
    path('edit_user/<num>', views.editUser),
    path('admin_user/<num>', views.addstaff),
    path('block_user/<num>', views.blockUser),
    path('delete_user/<num>', views.deleteUser),

    path('posts', views.showposts),
    path('show_post/<slug>', views.showPost),
    path('add_post', views.addPost),
    path('edit_post/<slug>', views.editPost),
    path('delete_post/<slug>', views.deletePost),

    path('categories', views.showcategory),
    path('add_category', views.addcategory),
    path('edit_category/<num>', views.editcategory),
    path('delete_category/<num>', views.deletecategory),

    path('words', views.showwords),
    path('add_word', views.addword),
    path('edit_word/<num>', views.editword),
    path('delete_word/<num>', views.deleteword),

]

from django.urls import path,include
from django.contrib.auth import views as authView
from loginRegister import views
from loginRegister import forms


urlpatterns = [
    path('login/', authView.LoginView.as_view(authentication_form=forms.AuthFormCheckStatus), name='login'),
    path('logout/', authView.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='home'),
]

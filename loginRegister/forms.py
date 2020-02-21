from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email=forms.EmailField(max_length=254)
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2', )

class AuthFormCheckStatus(AuthenticationForm):
    print("***inclass")
    
    def confirm_login_allowed(self,user):
        print("****user.is_actqwive++",user.is_staff)
        print("****user.is_actqwive++",user.is_active)
        if not user.is_active and not user.is_staff:
            print("*****active check")
            raise forms.ValidationError("YourAckjhesdjvmdfvmfdncount",code='inactive',)
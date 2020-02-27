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
    def confirm_login_allowed(self,user):
        if not user.profile.status:
            raise forms.ValidationError("your account is blocked contact the admin",code='inactive',)
            # print("notNione")

        # if user is not None and  user.is_active:
        # if not user.is_staff:

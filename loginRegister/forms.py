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
    error_messages = {
        'invalid_login':(
            "Please enter a correct username and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive':("This account is block."),
    }
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None :
                        self.confirm_login_allowed(user_temp)
                
                raise self.get_invalid_login_error()
        return self.cleaned_data

    #!anther way to check if block or not (status column)
    # def confirm_login_allowed(self,user):
    #     if not user.profile.status:
    #         raise forms.ValidationError("your account is blocked contact the admin",code='inactive',)
            # print("notNione")

        # if user is not None and  user.is_active:
        # if not user.is_staff:

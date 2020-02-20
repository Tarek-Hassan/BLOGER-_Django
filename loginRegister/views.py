from .forms import RegisterForm
from django.shortcuts import render ,redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest

# Create your views here.
def index(request):

    return render(request,'registration/index.html',)


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

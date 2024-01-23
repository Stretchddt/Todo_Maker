from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = forms.CreateUserForm()
        if request.method == 'POST':
            form = forms.CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {user}')
                return redirect('login')
    context={'form': form}
    return render(request, 'profiles/register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('home')
            else:
                messages.info(request, 'Username of passowrd is incorrect')
    return render(request, 'profiles/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    user = User.objects.filter()
    return render(request, 'profiles/profile.html')
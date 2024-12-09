from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['user_name'], cd['user_email'], cd['user_password'])
            messages.success(request, 'user created successfully', extra_tags='success')
            return redirect('logins')
    else:
        form = UserRegisterForm()
        return render(request, 'user_register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['user_name'], password=cd['user_password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'user logged in successfully', extra_tags='success')
                return redirect('logins')
            else:
                messages.error(request, 'password is wrong', extra_tags='danger')
                return redirect('user_login')
    else:
        form = UserLoginForm()
        return render(request, 'user_login.html', context={'form': form})

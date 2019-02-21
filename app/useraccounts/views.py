from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserProfileForm


def signup_view(request):
    context = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'SignUp Completed')
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    context['form'] = form
    return render(request, 'useraccounts/signup.html', context)


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            next_path = request.GET.get('next')
            messages.info(request, f'[{request.user.username}] Login')
            return redirect(next_path) if next_path else redirect('index')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'useraccounts/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        username = request.user.username
        logout(request)
        messages.info(request, f'[{username}] Logout Completed')
        return redirect('index')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Edited')
    form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'useraccounts/profile.html', context)

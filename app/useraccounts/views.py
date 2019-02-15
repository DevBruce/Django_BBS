from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm


def signup_view(request):
    context = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
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
            return redirect(next_path) if next_path else redirect('index')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'useraccounts/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm


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

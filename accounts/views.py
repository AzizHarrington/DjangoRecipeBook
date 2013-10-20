from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth

from .forms import RegistrationForm


def login(request):
    return render(request, 'login.html')


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect(reverse('loggedin'))
    else:
        return redirect(reverse('invalid'))


def loggedin(request):
    return render(request, 'loggedin.html', {'username': request.user.username})


def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('success'))
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def register_success(request):
    return render(request, 'register_success.html')
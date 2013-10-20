from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import RegistrationForm


def login(request):
    return render(request, 'login.html')


def auth_view(request):
    pass


def loggedin(request):
    pass


def invalid_login(request):
    pass


def logout(request):
    pass


def register_user(request):
    pass


def register_success(request):
    pass
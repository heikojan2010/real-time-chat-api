from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as execlogout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User


def login(request, *args, **kwargs):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(reverse('chat:myroom'))
        else:
            print(form.errors)
    return render(request, 'core/login.html', {'form': form})


def logout(request):
    logout(request)
    return redirect(reverse('chat:login'))


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('chat:login'))
        else:
            print(form.errors)
    return render(request, 'core/register.html', {'form': form})


def myroom(request):
    return render(request, 'core/myroom.html')

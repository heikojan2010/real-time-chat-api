from django.urls import path, re_path
from django.conf import settings
from operator import index
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from chat.core.views import register
from chat.core.views import login, logout, register, myroom


urlpatterns = [
    path('', login, name='login'),




    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^myroom$', myroom, name='myroom'),


]

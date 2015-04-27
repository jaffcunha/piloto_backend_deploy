from django.conf.urls import patterns, include, url
from django.contrib import admin
from newapp.views import *

urlpatterns = patterns('',
    url(r'^home/$', 'newapp.views.home', name='home'),
)

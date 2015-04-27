from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader, Context
from sistema.forms import *
from sistema.models import *
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib import auth
from django.conf import settings
import os
from os import path
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home1.html', locals())

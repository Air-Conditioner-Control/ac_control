from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
# from .models import *
import json


def home(request):
	return render(request, 'home/home.html', {})


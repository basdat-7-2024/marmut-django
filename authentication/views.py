from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def show_main(request):
    return render(request, "auth.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

# Create your views here.

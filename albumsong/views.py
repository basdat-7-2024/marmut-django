
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
import json

# Create your views here.

def albumsong(request):
    return render(request, 'albumsong.html')

def readalbum(request):
    return render(request, 'readalbum.html')

def albumkosong(request):
    return render(request, 'albumkosong.html')

def detaillagualbum(request):
    return render(request, 'detaillagualbum.html')

def listroyalti(request):
    return render(request, 'listroyalti.html')

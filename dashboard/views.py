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

def dashboard_podcaster(request):
    return render(request, "dashboard-podcaster.html")

def dashboard_podcaster_none(request):
    return render(request, "dashboard-podcaster-none.html")

def lihat_episode(request):
    return render(request, "lihat-episode.html")

def dashboard_label(request):
    return render(request, "dashboard-label.html")

def dashboard_pengguna(request):
    return render(request, "dashboard-pengguna.html")

def dashboard_singer(request):
    return render(request, "dashboard-singer.html")

def tes_create(request):
    return render(request, "create-podcast.html")




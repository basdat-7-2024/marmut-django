from django.db import connection
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
from dashboard.query import *
from podcast.views import *

def dashboard(request):
    set_role(request)

    request.session['list_podcast'] = []

    #Hanya buat testing nanti "tes" nya bisa dihapus
    request.session['list_playlist'] = ["tes"]

    if (request.session.get('role') == "Podcaster"):
        load_podcast(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'gender': request.session.get('gender'),
        'tempat_lahir': request.session.get('tempat_lahir'),
        'tanggal_lahir': request.session.get('tanggal_lahir'),
        'is_verified': request.session.get('is_verified'),
        'kota_asal': request.session.get('kota_asal'),
        'role': request.session.get('role'),
        'list_podcast': request.session.get('list_podcast'),
        'list_playlist': request.session.get('list_playlist'),
    }

    return render(request, "dashboard.html", context)

def dashboard_label(request):
    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
    }

    return render(request, "dashboard-label.html", context)

def set_role(request):
    cursor = connection.cursor()
    result_role = "Pengguna Biasa"

    cursor.execute(get_artist_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Artist"

    cursor.execute(get_songwriter_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Songwriter"

    cursor.execute(get_podcaster_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Podcaster"

    cursor.execute(get_premium_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        request.session['premium'] = True
    
    cursor.execute(get_nonpremium_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        request.session['premium'] = False

    request.session['role'] = result_role

def dashboard_pengguna(request):
    return render(request, "dashboard-pengguna.html")

def tes_create(request):
    return render(request, "create-podcast.html")

def dashboard_pengguna_none(request):
    return render(request, "dashboard-pengguna-none.html")

def song_detail(request):
    return render(request, "song-detail.html")

def playlist_detail(request):
    return render(request, "playlist-detail.html")

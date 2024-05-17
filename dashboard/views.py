from django.db import connection
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
import json
from albumsong.views import *
from dashboard.query import *
from podcast.views import *

def dashboard(request):
    set_role(request)

    status = "Non Premium"
    request.session['list_podcast'] = []

    #Hanya buat testing nanti "tes" nya bisa dihapus
    request.session['list_playlist'] = ["tes"]
    request.session['list_lagu_artist'] = ["tes"]
    request.session['list_lagu_songwriter'] = ["tes"]

    if ("Podcaster" in request.session.get('role')):
        load_podcast(request)
        
    if ("Artist" in request.session.get('role')):
        load_lagu_artist(request)

    if ("Songwriter" in request.session.get('role')):
        load_lagu_songwriter(request)

    if (request.session.get('premium')):
        status = "Premium"

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'gender': request.session.get('gender'),
        'tempat_lahir': request.session.get('tempat_lahir'),
        'tanggal_lahir': request.session.get('tanggal_lahir'),
        'is_verified': request.session.get('is_verified'),
        'kota_asal': request.session.get('kota_asal'),
        'status': status,
        'role': request.session.get('role'),
        'list_podcast': request.session.get('list_podcast'),
        'list_playlist': request.session.get('list_playlist'),
        'list_lagu_artist': request.session.get('list_lagu_artist'),
        'list_lagu_songwriter': request.session.get('list_lagu_songwriter'),
    }

    return render(request, "dashboard.html", context)

def dashboard_label(request):
    request.session['list_album'] = ["tes"]

    load_album_label(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
        'list_album': request.session.get('list_album'),
    }

    return render(request, "dashboard-label.html", context)

def set_role(request):
    cursor = connection.cursor()
    result_role = "Pengguna Biasa"
    list_role = ["Pengguna Biasa"]

    cursor.execute(get_artist_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Artist"
        list_role.append(result_role)

    cursor.execute(get_songwriter_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Songwriter"
        list_role.append(result_role)

    cursor.execute(get_podcaster_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Podcaster"
        list_role.append(result_role)

    cursor.execute(get_premium_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        request.session['premium'] = True
    
    cursor.execute(get_nonpremium_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        request.session['premium'] = False

    role_string = ', '.join(list_role)
    print(role_string)
    request.session['role'] = role_string

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

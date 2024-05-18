
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
from django.shortcuts import redirect
from django.urls import reverse
import json

from albumsong.query import *
from dashboard.query import *
from podcast.views import *

# Create your views here.

def load_album_label(request):
    cursor = connection.cursor()
    cursor.execute(get_information_album_label(request.session.get('email')))
    temp_id_album = cursor.fetchall()
    
    request.session['list_album'] = temp_id_album

def load_album_artist(request):
    cursor = connection.cursor()
    cursor.execute(get_information_album_artist(request.session.get('email')))
    temp_id_album = cursor.fetchall()
    
    request.session['list_album_artist'] = temp_id_album

def load_lagu_artist(request):
    cursor = connection.cursor()

    cursor.execute(get_information_lagu(request.session.get('email')))
    temp_id_lagu = cursor.fetchall()
    
    request.session['list_lagu_artist'] = temp_id_lagu

def load_lagu_songwriter(request):
    cursor = connection.cursor()

    cursor.execute(get_information_songwriter(request.session.get('email')))
    temp_id_lagu = cursor.fetchall()

    request.session['list_lagu_songwriter'] = temp_id_lagu


def load_lagu_album(request):
    cursor = connection.cursor()

    cursor.execute(get_information_lagu_album(request.session.get('album_title')))
    temp_id_lagu_album = cursor.fetchall()



    request.session['list_lagu_album'] = temp_id_lagu_album


def get_song_details(request):
    cursor = connection.cursor()

    cursor.execute(get_information_song_details(request.session.get('song_details')))
    temp_id_song_details = cursor.fetchall()

    request.session['song_details'] = temp_id_song_details

def albumsong(request):
    return render(request, 'albumsong.html')

def readalbum(request):
    return render(request, 'readalbum.html')

def detaillagualbum(request):
    return render(request, 'detaillagualbum.html')

def listroyalti(request):
    return render(request, 'listroyalti.html')

def readdeletealbum(request):
    return render(request, 'readdeletealbum.html')


def kelola_album(request):
    request.session['list_album'] = ["tes"]

    load_album_label(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
        'list_album': request.session.get('list_album'),
        
    }

    return render(request, 'kelola-album.html', context)

def kelola_album_artist(request):
    request.session['list_album_artist'] = ["tes"]

    load_album_artist(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
        'list_album_artist': request.session.get('list_album'),
        
    }

    return render(request, 'kelola-album.html', context)

def save_album_title(request, album_title):
    request.session['album_title'] = album_title
    return redirect(reverse('daftar_lagu'))

def daftar_lagu(request, album_title):
    request.session['album_title'] = album_title
    request.session['list_lagu_album'] = ["tes"]

    load_lagu_album(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
        'list_lagu_album': request.session.get('list_lagu_album'),
        'album_title': request.session.get('album_title'),
        'song_details': request.session.get('song_details'),
        'list_song_details': request.session.get('list_song_details'),
    }

    return render(request, 'daftar-lagu.html', context)




def song_details_modal(request, song_title):
    request.session['song_details'] = song_title
    request.session['list_song_details'] = ["tes"]

    context = {
        'song_details': request.session.get('song_details'),
        'list_song_details': request.session.get('list_song_details'),
    }
    return render(request, 'detail-song.html', context)

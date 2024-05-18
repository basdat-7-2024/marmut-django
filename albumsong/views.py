
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
from dashboard.views import *

# Create your views here.

def load_album_label(request):
    cursor = connection.cursor()
    cursor.execute(get_information_album_label(request.session.get('email')))
    temp_id_album = cursor.fetchall()
    
    request.session['list_album'] = temp_id_album

def load_album_artist_songwriter(request):
    cursor = connection.cursor()
    result_role = "Pengguna Biasa"
    list_role = ["Pengguna Biasa"]

    cursor.execute(get_artist_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Artist"
        list_role.append(result_role)
        cursor = connection.cursor()
        cursor.execute(get_information_album_artist(request.session.get('email')))

    if (result_role != "Artist"):    
        cursor.execute(get_songwriter_role(request.session.get('email')))
        temp_role = cursor.fetchall()
        if (temp_role != []):
            result_role = "Songwriter"
            list_role.append(result_role)
            cursor = connection.cursor()
            cursor.execute(get_information_album_songwriter(request.session.get('email')))


    temp_id_album = cursor.fetchall()

    
    request.session['list_album_artist_songwriter'] = temp_id_album
    role_string = ', '.join(list_role)
    request.session['role'] = role_string

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

def get_information_song_details(name):
    query = f"""
    SELECT 
        k.judul AS judul_lagu,
        STRING_AGG(DISTINCT g.genre, ', ') AS genres,
        a.email_akun AS artist_email,
        STRING_AGG(DISTINCT sw.email_akun, ', ') AS songwriter_emails,
        k.durasi,
        k.tanggal_rilis,
        k.tahun,
        s.total_play,
        s.total_download,
        al.judul AS judul_album
    FROM 
        SONG s
    JOIN 
        Konten k ON s.id_konten = k.id
    JOIN 
        ALBUM al ON s.id_album = al.id
    JOIN 
        ARTIST a ON s.id_artist = a.id
    JOIN 
        Genre g ON k.id = g.id_konten
    LEFT JOIN 
        SONGWRITER_WRITE_SONG sws ON s.id_konten = sws.id_song
    LEFT JOIN 
        SONGWRITER sw ON sws.id_songwriter = sw.id
    WHERE 
        k.judul = '{name}'
    GROUP BY 
        k.judul, a.email_akun, k.durasi, k.tanggal_rilis, k.tahun, s.total_play, s.total_download, al.judul;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
    
    return result

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

def kelola_album_artist_songwriter(request):
    request.session['list_album_artist_songwriter'] = ["tes"]

    load_album_artist_songwriter(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
        'list_album_artist_songwriter': request.session.get('list_album_artist_songwriter'),
        
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




def song_details_ajax(request, album_title, song_title):
    song_details = get_information_song_details(song_title)
    data = {
        'judul_lagu': song_details[0],
        'genres': song_details[1],
        'artist_email': song_details[2],
        'songwriter_emails': song_details[3],
        'durasi': song_details[4],
        'tanggal_rilis': song_details[5].strftime("%d/%m/%Y"),
        'tahun': song_details[6],
        'total_play': song_details[7],
        'total_download': song_details[8],
        'judul_album': song_details[9],
    }
    return JsonResponse(data)
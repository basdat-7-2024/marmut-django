from django.http import Http404, HttpResponse
from django.urls import reverse
from kelola_playlist import views
from django.db import connection
from django.shortcuts import redirect, render
from kelola_playlist.helper import *
from kelola_playlist.query import *
from dashboard.query import *

# Create your views here.
def kelola_playlist(request, *args, **kwargs):
    context = {
        'list_playlist': request.session.get('list_playlist'),
    }
    return render(request, "kelola-playlist.html", context)

def playlist_detail(request, *args, **kwargs):
    id = kwargs['id']
    cursor_info = connection.cursor()
    cursor_lagu = connection.cursor()
    if(not is_valid_uuid(id)):
        raise Http404
    
    cursor_info.execute(get_user_playlist_info_from_id(id))
    cursor_lagu.execute(get_user_playlist_songs_from_id(id))
    playlist_info_raw = cursor_info.fetchall()[0]
    lagu_in_playlist_raw = cursor_lagu.fetchall()

    if(playlist_info_raw == []):
        raise Http404
    
    lagu_in_playlist = []
    playlist_info = {}
    
    playlist_info['email_pembuat'] = playlist_info_raw[0]
    playlist_info['id_user_playlist'] = playlist_info_raw[1]
    playlist_info['judul'] = playlist_info_raw[2]
    playlist_info['jumlah_lagu'] = playlist_info_raw[3]
    playlist_info['tanggal_dibuat'] = playlist_info_raw[4]
    playlist_info['id_playlist'] = playlist_info_raw[5]
    playlist_info['total_durasi'] = f"{playlist_info_raw[6]} Menit" if playlist_info_raw[6] < 60 else f"{playlist_info_raw[6]//60} Jam {playlist_info_raw[6]%60} Menit"
    playlist_info['nama'] = playlist_info_raw[7]
    playlist_info['deskripsi'] = playlist_info_raw[8]

    for i in lagu_in_playlist_raw:
        temp = {}
        id_song = i[0]
        judul = i[1]
        durasi = i[2]
        artist = i[3]
        temp['id_song'] = id_song
        temp['judul'] = judul
        temp['durasi'] = f"{durasi} Menit" if durasi < 60 else f"{durasi//60} Jam {durasi%60} Menit"
        temp['artist'] = artist
        lagu_in_playlist.append(temp)

    context = {
        'playlist_info': playlist_info,
        'songs':lagu_in_playlist
    }
    return render(request, "playlist-detail.html", context)

def ubah_playlist(request):
    cursor = connection.cursor()
    if request.method == "POST":
        id = request.POST.get('id')
        title = request.POST.get('title')
        desc = request.POST.get('description')
        cursor.execute(update_playlist(id, title, desc))
    
    return redirect(reverse("dashboard:dashboard"))

def hapus_playlist(request, *args, **kwargs):
    cursor = connection.cursor()
    id = kwargs['id']
    cursor.execute(delete_playlist(id))

    return redirect(reverse("dashboard:dashboard"))
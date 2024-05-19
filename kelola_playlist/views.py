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

    data = load_all_song()
    print(data)
    context = {
        'playlist_info': playlist_info,
        'songs':lagu_in_playlist,
        'all_song': data,
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

def load_playlist(request):
    cursor = connection.cursor()
    cursor.execute(get_user_playlist(request.session.get('email')))
    list_playlist = cursor.fetchall()
    playlist_dashboard = []
    for i in list_playlist:
        temp={}
        temp['email_pembuat'] = i[0]
        temp['id_user_playlist'] = str(i[1])
        temp['judul'] = i[2]
        temp['deskripsi'] = i[3]
        temp['jumlah_lagu'] = i[4]
        temp['id_playlist'] = str(i[6])
        temp['durasi'] = f"{i[7]} Menit" if i[7] < 60 else f"{i[7]//60} Jam {i[7]%60} Menit"
        playlist_dashboard.append(temp)

    request.session['list_playlist'] = playlist_dashboard

def load_all_song():
    cursor = connection.cursor()
    cursor.execute("select id, judul from konten where id in (select id_konten from song)")
    data_raw = cursor.fetchall()
    data=[]
    for i in data_raw:
        temp={}
        temp['id'] = i[0]
        temp['judul'] = i[1]
        data.append(temp)
    return data

def tambah_lagu_playlist(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        id = request.POST.get('id')
        id_playlist = request.POST.get('id_playlist')
        cursor.execute(f"insert into playlist_song (id_playlist, id_song) values (\'{id_playlist}\', \'{id}\')")
        return redirect(reverse("kelola_playlist:playlist_detail", kwargs={'id': id_playlist}))
    return Http404
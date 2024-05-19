from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import render
from user_playlist.query import *
from user_playlist.helper import *

# Create your views here.

def user_playlist_detail(request, *args, **kwargs):
    id = kwargs['id']
    cursor_info = connection.cursor()
    cursor_lagu = connection.cursor()
    if(not is_valid_uuid(id)):
        raise Http404
    
    cursor_info.execute(get_playlist_info_from_id(id))
    cursor_lagu.execute(get_playlist_songs_from_id(id))
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
    # print(cursor.fetchall())
    return render(request, 'playlistdetail_by_user.html', context)

def shuffle_play(request):
    cursor = connection.cursor()

    email_pemain = request.session.get('email')
    id_playlist = request.GET.get('id')
    email_pembuat = request.GET.get('email_pembuat')
    # print(f'{email_pemain} {id_playlist} {email_pembuat}')

    cursor.execute(insert_into_akun_play_user_playlist(email_pemain, id_playlist, email_pembuat))
    return HttpResponse('OK')

def song_detail(request, *args, **kwargs):
    id = kwargs['id']
    cursor_info = connection.cursor()
    cursor_songwriter = connection.cursor()
    cursor_genre = connection.cursor()

    cursor_info.execute(get_song_detail_info_from_id(id))
    song_info = cursor_info.fetchone()


    
    cursor_songwriter.execute(get_songwriter_from_id(id))
    songwriter = cursor_songwriter.fetchall()
    songwriter= [i[0] for i in songwriter]

    cursor_genre.execute(get_genre_from_id(id))
    genre = cursor_genre.fetchall()
    genre = [i[0] for i in genre]
    print(songwriter)
    context = {
        'song_info' : {
            'id_konten': song_info[0],
            'id_artist': song_info[1],
            'id_album': song_info[2],
            'total_play': f"{song_info[3]:,.0f}",
            'total_download': f"{song_info[4]:,.0f}",
            'judul': song_info[5],
            'tanggal_rilis': song_info[6],
            'tahun': song_info[7],
            'durasi': f"{song_info[8]} Menit" if song_info[8] < 60 else f"{song_info[8]//60} Jam {song_info[8]%60} Menit",
            'nama_album': str(song_info[9]),
            'artist': song_info[10],
            'genre': genre,
            'songwriter': songwriter
        },
    }

    return render(request, 'song-detail.html', context)
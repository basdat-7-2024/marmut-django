from django.db import connection
from django.shortcuts import render

from kelola_playlist.query import *

# Create your views here.
def kelola_playlist(request):
    context = {
        'list_playlist': request.session.get('list_playlist')
    }
    return render(request, "kelola-playlist.html", context)

#ini udah gue siapin link buat back buttonnya
def playlist_detail(request):
    context = {
        'path_back_playlist': request.session.get('path_to_detail'),
    }
    return render(request, "playlist-detail.html", context)

#kalo mau load di kelola playlist pake ini aja juga zi, dah gue siapin fungsi2nya
def load_playlist(request):
    cursor = connection.cursor()
    request.session['path_to_detail'] = request.path

    cursor.execute(get_user_playlist(request.session.get('email')))
    temp_user_playlist = cursor.fetchall()
        
    request.session['list_playlist'] = temp_user_playlist
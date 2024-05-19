from django.urls import path
from kelola_playlist.views import *


app_name = 'kelola_playlist'

urlpatterns = [
    path('', kelola_playlist, name='kelola_playlist'),
    path('playlist-detail/', playlist_detail, name='playlist_detail'),
]
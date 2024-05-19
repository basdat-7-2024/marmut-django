from django.urls import path
from kelola_playlist.views import *


app_name = 'kelola_playlist'

urlpatterns = [
    path('', kelola_playlist, name='kelola_playlist'),
    path('detail/<str:id>', playlist_detail, name='playlist_detail'),
    path('ubah-playlist', ubah_playlist, name="ubah_playlist"),
    path('hapus-playlist/<str:id>', hapus_playlist, name="hapus_playlist"),
]
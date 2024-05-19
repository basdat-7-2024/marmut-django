from django.urls import path
from albumsong.views import *


app_name = 'albumsong'

urlpatterns = [
    path('', albumsong, name='albumsong'),
    path('readalbum/', readalbum, name='readalbum'),
    path('detaillagualbum/', detaillagualbum, name='detaillagualbum'),
    path('listroyalti/', listroyalti, name='listroyalti'),
    path('readdeletealbum/', readdeletealbum, name='readdeletealbum'),
    path('kelola_album/', kelola_album, name='kelola_album'),
    path('kelola_album_artist_songwriter/', kelola_album_artist_songwriter, name='kelola_album_artist_songwriter'),
    path('save-album-title/<str:album_title>/', save_album_title, name='save_album_title'),
    path('daftar_lagu/<str:album_title>/', daftar_lagu, name='daftar_lagu'),
    path('song_details_ajax/<str:album_title>/<str:song_title>/', song_details_ajax, name='song_details_ajax'),
    path('add_album_ajax/', add_album_ajax, name='add_album_ajax')
]

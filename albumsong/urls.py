from django.urls import path
from albumsong.views import *


app_name = 'albumsong'

urlpatterns = [
    path('', albumsong, name='albumsong'),
    path('readalbum/', readalbum, name='readalbum'),
    path('albumkosong/', albumkosong, name='albumkosong'),
    path('detaillagualbum/', detaillagualbum, name='detaillagualbum'),
    path('listroyalti/', listroyalti, name='listroyalti'),
    path('readdeletealbum/', readdeletealbum, name='readdeletealbum'),
    path('kelola_album/', kelola_album, name='kelola_album'),
    path('save-album-title/<str:album_title>/', save_album_title, name='save_album_title'),
    path('daftar_lagu/<str:album_title>/', daftar_lagu, name='daftar_lagu')
]

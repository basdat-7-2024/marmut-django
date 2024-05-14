from django.urls import path
from dashboard.views import *


app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('lihat-episode/', lihat_episode, name='lihat_episode'),
    path('tes/', tes_create, name='tes_create'),
    path('label/', dashboard_label, name='dashboard_label'),
    path('pengguna/', dashboard_pengguna, name='dashboard_pengguna'),
    path('pengguna-none/', dashboard_pengguna_none, name='dashboard-pengguna-none'),
    path('song-detail/', song_detail, name='song_detail'),
    path('playlist-detail/', playlist_detail, name='playlist_detail'),
]
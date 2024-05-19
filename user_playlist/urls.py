from django.urls import path
from user_playlist.views import *


app_name = 'user_playlist'

urlpatterns = [
    path('shuffle-play/', shuffle_play, name='shuffle_play'),
    path('song-detail/<str:id>', song_detail, name='song_detail'),
]

from django.urls import path
from user_playlist.views import *


app_name = 'user_playlist'

urlpatterns = [
    path('', user_playlist_detail, name='user_playlist_detail'),
]

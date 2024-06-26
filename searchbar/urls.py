from django.urls import path
from podcast.views import podcast_detail
from searchbar.views import *
from user_playlist.views import *


app_name = 'searchbar'

urlpatterns = [
    path('<str:query>/', searchpage, name='searchpage'),
    path('podcast/<str:podcast_id>/', podcast_detail, name='podcast_detail'),
    path('playlist/<str:id>/', user_playlist_detail, name='user_playlist_detail'),
    path('song/<str:id>/', song_detail, name='song_detail'),
]
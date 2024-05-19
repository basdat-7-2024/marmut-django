from django.urls import path
from searchbar.views import *
from user_playlist.views import *


app_name = 'searchbar'

urlpatterns = [
    path('<str:query>/', searchpage, name='searchpage'),
    path('playlist/<str:id>/', user_playlist_detail, name='user_playlist_detail'),
]
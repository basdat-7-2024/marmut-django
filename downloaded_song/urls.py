from django.urls import path
from downloaded_song.views import *


app_name = 'downloaded_song'

urlpatterns = [
    path('', daftardownload, name='daftardownload'),
]

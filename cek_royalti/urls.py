from django.urls import path
from cek_royalti.views import *


app_name = 'cek_royalti'

urlpatterns = [
    path('', cek_royalti_label, name='cek_royalti_label'),
    path('cek_royalti_artist_songwriter/', cek_royalti_artist_songwriter, name='cek_royalti_artist_songwriter'),
]
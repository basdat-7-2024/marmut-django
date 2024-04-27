from django.urls import path
from langganan_paket.views import *


app_name = 'langganan_paket'

urlpatterns = [
    path('', listpaket, name='listpaket'),
    path('riwayat/', riwayatpaket, name='riwayatpaket'),
    path('pembayaran/', pembayaranpaket, name='pembayaranpaket'),
]

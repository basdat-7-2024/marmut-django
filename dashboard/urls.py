from django.urls import path
from dashboard.views import *


app_name = 'dashboard'

urlpatterns = [
    path('podcaster/', dashboard_podcaster, name='dashboard_podcaster'),
    path('label/', dashboard_label, name='dashboard_label'),
    path('pengguna/', dashboard_pengguna, name='dashboard_pengguna'),
    path('singer/', dashboard_singer, name='dashboard_singer'),
]
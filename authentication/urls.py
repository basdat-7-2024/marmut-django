from django.urls import path
from authentication.views import *


app_name = 'authentication'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('pilih-register/', pilih_register, name='pilih_register'),
    path('register-label/', register_label, name='register_label'),
]

from django.urls import path
from authentication.views import *


app_name = 'authentication'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('pilih-register/', pilih_register, name='pilih_register')
]

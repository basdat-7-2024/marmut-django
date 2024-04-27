from django.urls import path
from authentication.views import *


app_name = 'authentication'

urlpatterns = [
    path('', show_main, name='show_main'),
]

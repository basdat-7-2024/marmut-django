from django.urls import path
from searchbar.views import *


app_name = 'searchbar'

urlpatterns = [
    path('<str:query>/', searchpage, name='searchpage'),
]
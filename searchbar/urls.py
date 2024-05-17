from django.urls import path
from podcast.views import podcast_detail
from searchbar.views import *


app_name = 'searchbar'

urlpatterns = [
    path('<str:query>/', searchpage, name='searchpage'),
    path('podcast/<str:podcast_id>/', podcast_detail, name='podcast_detail'),
]
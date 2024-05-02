from django.urls import path
from podcast.views import *


app_name = 'podcast'

urlpatterns = [
    path('detail/', podcast_detail, name='podcast_detail'),
    path('kelola/', kelola_podcast, name='kelola_podcast'),
]
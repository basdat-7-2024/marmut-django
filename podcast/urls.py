from django.urls import path
from podcast.views import *


app_name = 'podcast'

urlpatterns = [
    path('detail/', podcast_detail, name='podcast_detail'),
    path('kelola/', kelola_podcast, name='kelola_podcast'),
    path('kelola-none/', kelola_podcast_none, name='kelola_podcast_none'),
    path('lihat-episode/', lihat_episode, name='lihat_episode'),
]
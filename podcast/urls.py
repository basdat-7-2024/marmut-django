from django.urls import path
from podcast.views import *


app_name = 'podcast'

urlpatterns = [
    path('detail/', podcast_detail, name='podcast_detail'),
    path('kelola/', kelola_podcast, name='kelola_podcast'),
    path('lihat-episode-kelola/', lihat_episode_kelola, name='lihat_episode_kelola'),
    path('lihat-episode-dashboard/', lihat_episode_dashboard, name='lihat_episode_dashboard'),
]
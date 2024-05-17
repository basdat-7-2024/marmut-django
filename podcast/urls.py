from django.urls import path
from podcast.views import *


app_name = 'podcast'

urlpatterns = [
    path('kelola/', kelola_podcast, name='kelola_podcast'),
    path('create-podcast/', create_podcast, name='create_podcast'),
    path('create-episode/', create_episode, name='create_episode'),
    path('delete-podcast/<str:podcast_id>/', delete_podcast, name='delete_podcast'),
    path('delete-episode/<str:podcast_id>/<str:episode_id>/', delete_episode, name='delete_episode'),
    path('lihat-episode-kelola/', lihat_episode_kelola, name='lihat_episode_kelola'),
    path('lihat-episode-dashboard/<str:judul_podcast>/<str:podcast_id>/', lihat_episode_dashboard, name='lihat_episode_dashboard'),
]
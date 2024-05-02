from django.urls import path
from chart.views import *


app_name = 'podcast'

urlpatterns = [
    path('detail/', podcast_detail, name='podcast_detail'),
]
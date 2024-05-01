from django.urls import path
from dashboard.views import *


app_name = 'dashboard'

urlpatterns = [
    path('podcaster/', dashboard_podcaster, name='dashboard_podcaster'),
]
from django.urls import path
from albumsong.views import *


app_name = 'albumsong'

urlpatterns = [
    path('', albumsong, name='albumsong'),
    path('readalbum/', readalbum, name='readalbum'),
    path('albumkosong/', albumkosong, name='albumkosong'),
    path('detaillagualbum/', detaillagualbum, name='detaillagualbum'),
    path('listroyalti/', listroyalti, name='listroyalti'),
    path('readdeletealbum/', readdeletealbum, name='readdeletealbum'),
]

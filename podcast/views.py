from django.db import connection
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from podcast.query import *

def podcast_detail(request):
    return render(request, "podcastdetail.html")

def count_episode(request, id_konten):
    cursor = connection.cursor()
    cursor.execute(get_episode_podcast(id_konten))
    return cursor.fetchall()

def load_podcast(request):
    cursor = connection.cursor()
    list_podcast = []

    cursor.execute(get_konten_podcast(request.session.get('email')))
    temp_id_konten = cursor.fetchall()
    
    for id in temp_id_konten:
        cursor.execute(get_information_podcast(id[0]))
        info_podcast = cursor.fetchall()

        #Menghitung jumlah episode dari tiap podcast
        temp_count_episode = count_episode(request, id[0])
        sum_episode = len(temp_count_episode)
        
        temp_list = list(info_podcast[0])
        temp_list.append(sum_episode)

        #Mengubah format date agar bisa masuk ke session
        temp_list[1] = temp_list[1].isoformat()

        list_podcast.append(temp_list)
    
    request.session['list_podcast'] = list_podcast

def kelola_podcast(request):
    load_podcast(request)

    temp_list_podcast = request.session['list_podcast']
    
    context = {
        'list_podcast': temp_list_podcast,
    }

    return render(request, "kelola-podcast.html", context)

def lihat_episode(request):
    return render(request, "lihat-episode-2.html")
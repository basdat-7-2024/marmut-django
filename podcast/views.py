import uuid
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

def podcast_detail(request, podcast_id):
    cursor = connection.cursor()
    cursor.execute(get_detail_podcast(podcast_id))
    temp_detail = cursor.fetchall()
    temp_detail = temp_detail[0]

    cursor.execute(get_episode_podcast(podcast_id))
    temp_detail_episode = cursor.fetchall()

    context = {
        'temp_path': request.session.get('temp_path'),
        'list_detail_podcast': temp_detail,
        'list_detail_episode': temp_detail_episode,
    }
    print(temp_detail)

    return render(request, "podcast-detail.html", context)


def count_episode(request, id_konten):
    cursor = connection.cursor()
    cursor.execute(get_episode_podcast(id_konten))
    return cursor.fetchall()

def load_podcast(request):
    cursor = connection.cursor()
    list_podcast = []
    request.session['temp_podcaster_path'] = request.path

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
        temp_list[4] = str(temp_list[4])

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
    
def create_podcast(request):
    cursor = connection.cursor()
    random_uuid = uuid.uuid4()
    today = datetime.date.today()
    year = today.year
    genres = []

    print(request.session.get('temp_podcaster_path'))

    if request.method == 'POST':
        title = request.POST.get('title')
        duration = request.POST.get('duration')

        if 'Action' in request.POST:
            genres.append(request.POST['Action'])
        if 'Romance' in request.POST:
            genres.append(request.POST['Romance'])
        if 'Comedy' in request.POST:
            genres.append(request.POST['Comedy'])
        
        genre_string = ', '.join(genres)

        cursor.execute(create_konten_podcast(random_uuid, title, today, year, duration))
        cursor.execute(create_tabel_podcast(random_uuid, request.session.get('email')))
        cursor.execute(create_genre_podcast(random_uuid, genre_string))

        return redirect('dashboard:dashboard')
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
def delete_podcast(request, podcast_id):
    cursor = connection.cursor()
    cursor.execute(delete_podcast_from_id_konten(podcast_id))
    return redirect('dashboard:dashboard')

def create_episode(request):
    random_uuid = uuid.uuid4()
    today = datetime.date.today()

    if request.method == 'POST':
        episode_title = request.POST.get('title')
        duration = request.POST.get('duration')
        podcast_id = request.POST.get('podcast_id')
        description = request.POST.get('description')

        cursor = connection.cursor()
        cursor.execute(create_episode_on_tabel(random_uuid, podcast_id, episode_title, description, duration, today))

        return redirect('dashboard:dashboard')
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
def delete_episode(request, podcast_id, episode_id):
    cursor = connection.cursor()
    cursor.execute(delete_episode_from_tabel(episode_id))

    cursor.execute(get_information_podcast(podcast_id))
    temp_podcast = cursor.fetchall()
    judul = temp_podcast[0][0]

    return redirect('podcast:lihat_episode_dashboard', podcast_id=podcast_id, judul_podcast=judul)

def lihat_episode_kelola(request):
    return render(request, "lihat-episode-2.html")

def lihat_episode_dashboard(request, judul_podcast, podcast_id):
    cursor = connection.cursor()
    cursor.execute(get_episode_from_tabel(podcast_id))
    temp_episode = cursor.fetchall()

    context = {
        'list_episode': temp_episode,
        'judul_podcast': judul_podcast,
        'podcast_id': podcast_id,
    }

    return render(request, "lihat-episode.html", context)
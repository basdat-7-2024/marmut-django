
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

from albumsong.query import *

# Create your views here.

def load_album_label(request):
    cursor = connection.cursor()

    cursor.execute(get_information_album_label(request.session.get('email')))
    temp_id_album = cursor.fetchall()
    
    request.session['list_album'] = temp_id_album

def load_lagu_artist(request):
    cursor = connection.cursor()

    cursor.execute(get_information_lagu(request.session.get('email')))
    temp_id_lagu = cursor.fetchall()
    
    request.session['list_lagu_artist'] = temp_id_lagu

def load_lagu_songwriter(request):
    cursor = connection.cursor()

    cursor.execute(get_information_songwriter(request.session.get('email')))
    temp_id_lagu = cursor.fetchall()

    print(temp_id_lagu)
    
    request.session['list_lagu_songwriter'] = temp_id_lagu

def albumsong(request):
    return render(request, 'albumsong.html')

def readalbum(request):
    return render(request, 'readalbum.html')

def albumkosong(request):
    return render(request, 'albumkosong.html')

def detaillagualbum(request):
    return render(request, 'detaillagualbum.html')

def listroyalti(request):
    return render(request, 'listroyalti.html')

def readdeletealbum(request):
    return render(request, 'readdeletealbum.html')

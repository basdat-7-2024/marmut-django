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
from dashboard.query import *
from cek_royalti.query import *
from albumsong.views import *


# Create your views here.
def load_royalti_label(request):
    cursor = connection.cursor()

    cursor.execute(get_information_royalti_label(request.session.get('email')))
    temp_id_royalti = cursor.fetchall()
    
    request.session['list_royalti'] = temp_id_royalti


def load_royalti_artist_songwriter(request):
    cursor = connection.cursor()
    result_role = "Pengguna Biasa"
    list_role = ["Pengguna Biasa"]



    cursor.execute(get_artist_role(request.session.get('email')))
    temp_role = cursor.fetchall()
    if (temp_role != []):
        result_role = "Artist"
        list_role.append(result_role)
        cursor = connection.cursor()
        cursor.execute(get_information_royalti_artist(request.session.get('email')))

    if (result_role != "Artist"):
        cursor.execute(get_information_royalti_songwriter(request.session.get('email')))
        temp_id_royalti = cursor.fetchall()
        if (temp_role != []):
            result_role = "Songwriter"
            list_role.append(result_role)
            cursor = connection.cursor()
            cursor.execute(get_information_royalti_songwriter(request.session.get('email')))

    temp_id_royalti = cursor.fetchall()
    
    request.session['list_royalti_artist_songwriter'] = temp_id_royalti
    role_string = ', '.join(list_role)
    request.session['role'] = role_string




def cek_royalti_label(request):
    request.session['list_royalti'] = ["tes"]

    load_royalti_label(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
        'list_album': request.session.get('list_album'),
        'list_royalti': request.session.get('list_royalti'),
        
    }




    return render(request, "kelola-royalti.html", context)

def cek_royalti_artist_songwriter(request):
    request.session['list_royalti_artist_songwriter'] = ["tes"]

    load_royalti_artist_songwriter(request)

    context = {
        'email': request.session.get('email'),
        'nama': request.session.get('nama'),
        'kontak': request.session.get('kontak'),
        'role': request.session.get('role'),
        'list_album': request.session.get('list_album'),
        'list_royalti_artist_songwriter': request.session.get('list_royalti_artist_songwriter'),
        
    }

    return render(request, "kelola-royalti.html", context)


    


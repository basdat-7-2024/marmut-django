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
from django.db import connection
from django.http import JsonResponse
from authentication.query import *

def show_main(request):
    return render(request, "auth.html")

def first_init(request):
    cursor = connection.cursor()

    cursor.execute(get_nama_akun(request.session.get('email')))
    request.session['nama'] = cursor.fetchone()[0]

    cursor.execute(get_gender_akun(request.session.get('email')))
    request.session['gender'] = cursor.fetchone()[0]

    # cursor.execute(get_tempat_lahir_akun(request.session.get('email')))
    # request.session['tempat_lahir'] = cursor.fetchone()[0]

    # cursor.execute(get_tanggal_lahir_akun(request.session.get('email')))
    # request.session['tanggal_lahir'] = cursor.fetchone()[0]

    # cursor.execute(get_is_verified_akun(request.session.get('email')))
    # request.session['is_verified'] = cursor.fetchone()[0]

    # cursor.execute(get_kota_asal_akun(request.session.get('email')))
    # request.session['kota_asal'] = cursor.fetchone()[0]

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        cursor = connection.cursor()
        cursor.execute(get_email_password(email, password))
        account = cursor.fetchone()

        if account:
            print(1)
            messages.success(request, "Login berhasil!")
            request.session['email'] = email
            first_init(request)

            return HttpResponseRedirect(reverse("dashboard:dashboard"))
        else:
            print(0)
            messages.error(request, "Login gagal! Email atau password salah.")
    
    return render(request, 'login.html')

def register(request):
    return render(request, "register.html")

def pilih_register(request):
    return render(request, "pilih-register.html")

def register_label(request):
    return render(request, "register-label.html")

def logout(request):
    request.session.flush()
    return render(request, "login.html")
# Create your views here.

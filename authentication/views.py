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

def init_non_label(request):
    cursor = connection.cursor()

    cursor.execute(get_nama_akun(request.session.get('email')))
    request.session['nama'] = cursor.fetchone()[0]

    cursor.execute(get_gender_akun(request.session.get('email')))
    temp_gender = cursor.fetchone()[0]
    if temp_gender == 0:
        temp_gender = "Perempuan"

    elif temp_gender == 1:
        temp_gender = "Laki-laki"

    request.session['gender'] = temp_gender

    cursor.execute(get_tempat_lahir_akun(request.session.get('email')))
    request.session['tempat_lahir'] = cursor.fetchone()[0]

    cursor.execute(get_tanggal_lahir_akun(request.session.get('email')))
    request.session['tanggal_lahir'] = cursor.fetchone()[0].isoformat()

    cursor.execute(get_is_verified_akun(request.session.get('email')))
    request.session['is_verified'] = cursor.fetchone()[0]

    cursor.execute(get_kota_asal_akun(request.session.get('email')))
    request.session['kota_asal'] = cursor.fetchone()[0]

def init_label(request):
    cursor = connection.cursor()

    cursor.execute(get_nama_label(request.session.get('email')))
    request.session['nama'] = cursor.fetchone()[0]

    cursor.execute(get_kontak_label(request.session.get('email')))
    request.session['kontak'] = cursor.fetchone()[0]

    request.session['role'] = "Label"

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        cursor_non_label = connection.cursor()
        cursor_label = connection.cursor()

        cursor_non_label.execute(get_email_password_from_akun(email, password))
        cursor_label.execute(get_email_password_from_label(email, password))

        account_non_label = cursor_non_label.fetchone()
        account_label = cursor_label.fetchone()

        #Saat login sebagai label
        if account_label:
            request.session['email'] = email
            request.session['is_login'] = True
            init_label(request)
            messages.success(request, "Login berhasil!")
            return HttpResponseRedirect(reverse("dashboard:dashboard_label"))

        #Saat login sebagai non label
        elif account_non_label:
            request.session['email'] = email
            request.session['is_login'] = True
            init_non_label(request)
            messages.success(request, "Login berhasil!")
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
            
        #Saat tidak berhasil login
        else:
            request.session['is_login'] = False
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
    return render(request, "auth.html")

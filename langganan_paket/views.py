
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
from langganan_paket.query import *
from django.db import connection
from django.http import JsonResponse


def listpaket(request):
    cursor = connection.cursor()
    cursor.execute(get_jenis_paket())
    temp = cursor.fetchall()
    context = {
        'jenis_harga': temp,
    }
    if request.method=="POST":
        request.session['old_request']=request.POST
        return HttpResponseRedirect('pembayaran')
    return render(request, "listpaket.html", context)


def riwayatpaket(request):
    # Fetch email from session
    user_email = request.session.get('email')
    
    # Check if the email exists in the session
    if not user_email:
        # Redirect to a valid error page if no email is found
        return redirect('login')  # Assuming 'login' is a valid URL pattern

    query = get_history_paket(user_email)
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    
    transactions = [
        {
            'Judul': row[0],
            'Tanggal_Dimulai': row[1],
            'Tanggal_Berakhir': row[2],
            'Metode_Pembayaran': row[3],
            'Nominal': row[4],
        }
        for row in rows
    ]
    
    context = {
        'transactions': transactions
    }
    return render(request, "riwayatpaket.html", context)

def pembayaranpaket(request):
    cursor = connection.cursor()
    cursor.execute(get_jenis_paket())
    temp = cursor.fetchall()
    temp = [x for x in temp if request.session['old_request']['jenis_paket'].replace('(', '').replace(')', '')in x]
    
    context = {
        'jenis_harga': temp,
    }
    print(temp)
    return render(request, "pembayaranpaket.html", context)



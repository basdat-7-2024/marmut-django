from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from django.utils import timezone
from .query import get_jenis_paket,get_history_paket, get_latest_end_date
import datetime
import uuid 

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
    user_email = request.session.get('email')
    
    if not user_email:
        return redirect('login')  

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
    selected_package = request.session.get('old_request')['jenis_paket']
    temp = [x for x in temp if selected_package in x]
    
    context = {
        'jenis_harga': temp,
    }

    user_email = request.session.get('email')

    if not user_email:
        return redirect('login')

    if request.method == "POST":
        jenis_paket = selected_package
        metode_bayar = request.POST.get('metode_bayar')

        cursor.execute(get_latest_end_date(user_email))
        latest_end_date_result = cursor.fetchone()
        if latest_end_date_result and latest_end_date_result[0]:
            timestamp_dimulai = latest_end_date_result[0]
        else:
            timestamp_dimulai = timezone.now()
        timestamp_berakhir = calculate_end_date(jenis_paket, timestamp_dimulai)
        nominal = get_nominal(jenis_paket)
        
        if user_email:
            try:
                # Generate a unique ID for the transaction
                transaction_id = str(uuid.uuid4())
                
                cursor.execute(
                    "INSERT INTO transaction (id, jenis_paket, email, timestamp_dimulai, timestamp_berakhir, metode_bayar, nominal) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    [transaction_id, jenis_paket, user_email, timestamp_dimulai, timestamp_berakhir, metode_bayar, nominal]
                )
                cursor.execute(
                    "INSERT INTO premium (email) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM premium WHERE email = %s)",
                    [user_email, user_email]
                )
                connection.commit()
                return redirect('langganan_paket:riwayatpaket')
            except Exception as e:
                context['error'] = str(e)
        else:
            context['error'] = 'Email not found in session'
        
    return render(request, "pembayaranpaket.html", context)

def calculate_end_date(jenis_paket, timestamp_dimulai):
    if jenis_paket == "1 Bulan":
        return timestamp_dimulai + datetime.timedelta(days=30)
    elif jenis_paket == "3 Bulan":
        return timestamp_dimulai + datetime.timedelta(days=90)
    elif jenis_paket == "6 Bulan":
        return timestamp_dimulai + datetime.timedelta(days=180)
    elif jenis_paket == "1 Tahun":
        return timestamp_dimulai + datetime.timedelta(days=365)
    return timestamp_dimulai

def get_nominal(jenis_paket):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT harga FROM paket WHERE jenis = '{jenis_paket}'")
        result = cursor.fetchone()
    return result[0] if result else 0
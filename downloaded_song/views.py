from django.shortcuts import render, redirect
from django.db import connection
from .query import get_downloaded_song

def daftardownload(request):
    user_email = request.session.get('email')
    
    if not user_email:
        # Redirect to a valid error page or login page if no email is found
        return redirect('login')  # Assuming 'login' is a valid URL pattern
    
    query = get_downloaded_song(user_email)
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    
    downloaded_songs = [
        {
            'Judul': row[0],
            'id_konten': row[1],
            'Tanggal_Download': row[2],
        }
        for row in rows
    ]
    
    context = {
        'downloaded_songs': downloaded_songs
    }
    return render(request, "daftar_download.html", context)

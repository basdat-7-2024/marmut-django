from django.shortcuts import render, redirect
from django.db import connection
from .query import get_downloaded_song

def daftardownload(request):
    user_email = request.session.get('email', None)
    if not user_email:
        return redirect('login')  # Redirect to login if the user is not logged in

    query = get_downloaded_song(user_email)
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    
    downloaded_song = [
        {
            'Judul': row[0],
        }
        for row in rows
    ]

    context = {'downloaded_song': downloaded_song}
    return render(request, "daftar_download.html", context)
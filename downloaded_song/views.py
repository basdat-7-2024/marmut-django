from django.shortcuts import render, redirect
from django.db import connection
from .query import get_downloaded_song, delete_downloaded_song

def daftardownload(request):
    user_email = request.session.get('email', None)
    if not user_email:
        return redirect('login')  # Redirect to login if the user is not logged in

    delete_success = False
    song_title = ""

    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        song_title = request.POST.get('song_title')
        if song_id:
            delete_query = delete_downloaded_song(user_email, song_id)
            try:
                with connection.cursor() as cursor:
                    cursor.execute(delete_query)
                delete_success = True
            except Exception as e:
                delete_success = False

    query = get_downloaded_song(user_email)
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    # Ensure rows have the expected number of columns
    downloaded_song = []
    for row in rows:
        if len(row) >= 2:
            downloaded_song.append({
                'id': row[0],
                'Judul': row[1],
            })

    context = {
        'downloaded_song': downloaded_song,
        'delete_success': delete_success,
        'deleted_song_title': song_title,
    }
    return render(request, "daftar_download.html", context)
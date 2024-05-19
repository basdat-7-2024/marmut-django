from django.shortcuts import render

# Create your views here.
def kelola_playlist(request):
    return render(request, "kelola-playlist.html")

def playlist_detail(request):
    return render(request, "playlist-detail.html")
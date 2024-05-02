from django.shortcuts import render

# Create your views here.

def user_playlist_detail(request):
    return render(request, 'playlistdetail_by_user.html')
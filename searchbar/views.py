from django.shortcuts import render



def searchpage(request, query):
    # Proses query untuk mendapatkan hasil pencarian
    # Misalnya, filter objek atau jalankan query database

    context = {
        'query': query,
        'results': []  # Gantikan dengan hasil pencarian sesungguhnya
    }
    return render(request, 'searchpage.html', context)

# views.py
from django.db import connection
from django.shortcuts import render
from .query import get_search_query  # Ensure this import reflects your project structure

def searchpage(request, query):
    request.session['temp_path'] = request.path
    results = perform_search(query) if query else []
    return render(request, 'searchpage.html', {'query': query, 'results': results})

def perform_search(query):
    search_query = get_search_query()
    with connection.cursor() as cursor:
        search_pattern = '%' + query + '%'
        cursor.execute(search_query, [search_pattern, search_pattern, search_pattern])
        results = cursor.fetchall()
    return results
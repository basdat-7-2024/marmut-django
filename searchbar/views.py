# views.py
from django.db import connection
from django.shortcuts import render
from django.utils.html import escape
from .query import get_search_query  # Ensure this import reflects your project structure

def searchpage(request, query):
    results = perform_search(query) if query else []
    return render(request, 'searchpage.html', {'query': query, 'results': results})

def perform_search(query):
    # Fetch the SQL query from query.py
    search_query = get_search_query()
    with connection.cursor() as cursor:
        search_pattern = '%' + query + '%'
        cursor.execute(search_query, [search_pattern, search_pattern, search_pattern])
        results = cursor.fetchall()
    return results

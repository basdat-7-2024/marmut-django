from django.db import connection
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

from chart.query import *

def chart_list(request):
    cursor = connection.cursor()
    cursor.execute(get_chart())
    temp_chart = cursor.fetchall()

    context = {
        'list_chart': temp_chart
    }

    return render(request, "chart-list.html", context)

def chart_detail(request):
    cursor = connection.cursor()
    cursor.execute(get_all_chart())
    temp_chart_detail = cursor.fetchall()

    context = {
        'list_chart_detail': temp_chart_detail
    }

    return render(request, "chart-detail.html", context)
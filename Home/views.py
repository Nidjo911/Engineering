from datetime import datetime
from django.http import HttpResponse
""" from django.http.request import HttpRequest """
from django.shortcuts import render

def home(request):
    return render(request, 'Home.html', {'time': datetime.now().strftime('%H:%M:%S')})

def about(request):
    return HttpResponse('About')
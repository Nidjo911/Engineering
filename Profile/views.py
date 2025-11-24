from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def profile(request):
    return render(request, 'products/products_home.html', {})

def profile_new(request):
    return render(request, 'products/products_home.html', {})
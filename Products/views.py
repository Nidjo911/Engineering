from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def products_home(request):
    print("Products home view was called!")
    products = list(Product.objects.all())
    print(f"Found {len(products)} products")
    for p in products:
        print(f"Product: {p.name}, Price: {p.price}")
    return render(request, 'products/products_home.html', {'products': products})


from django.shortcuts import render

products=["Product 1", "Product 2", "Product 3"]

# Create your views here.
def products_home(request):
    return render(request, 'products/products_home.html', {'products': products})
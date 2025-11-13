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


def product_detail(request, product_slug):
    try:
        print("Product detail view was called!")
        #return HttpResponse(product_slug)
        selected_product = Product.objects.get(slug=product_slug)
        #return HttpResponse(selected_product.name)
        return render(request, 'products/products_details.html', {'product_name': selected_product.name, 'product_price': selected_product.price, 'product_description': selected_product.description})
    except Exception as exc:
        return HttpResponse(f"Error: {exc}")
        

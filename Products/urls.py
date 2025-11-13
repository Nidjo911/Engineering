from django.urls import path
from . import views
urlpatterns = [
    path('', views.products_home, name='products-home'),
    path('<slug:product_slug>/', views.product_detail, name='product-detail'),
]

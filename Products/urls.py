from django.urls import path
from . import views
urlpatterns = [
    path('', views.products_home, name='products-home'),
    path('<slug:slug>/', views.product_detail, name='product-detail'),
]

from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.home, name='products-home'),
    path('about/', views.about, name='about'),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.products-home, name='products-home'),
]

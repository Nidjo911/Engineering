from django.urls import path

from . import views

urlpatterns = [
    path("new/", views.create_client, name="clients-create"),
    path("list/", views.list_clients, name="clients-list"),
]

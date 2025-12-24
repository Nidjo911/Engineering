from django.shortcuts import render
from .models import Client
from data import DUMMY_CLIENTS

# Create your views here.

from .forms import ClientForm


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientForm()
    else:
        form = ClientForm()

    return render(request, 'clients/ClientForm.html', {'form': form})


def list_clients(request):
    clients = DUMMY_CLIENTS
    return render(request, 'clients/clients_list.html', {'clients': clients})

from django.shortcuts import render

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

    return render(request, 'ClientForm.html', {'form': form})

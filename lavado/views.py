from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'Pipo'})


def index(request):
    return render(request, 'index.html')

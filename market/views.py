from django.shortcuts import render
from .models import Properties

def home(request):
    context = {
        'login' : False
    }
    return render(request, 'market/home.html', context)

def dashboard(request):
    properties = Properties.objects.all()

    context = {
        'login' : False, 
        'properties' : properties
    }
    return render(request, 'market/dashboard.html', context)

def about(request):
    context = {
        'login' : False
    }
    return render(request, 'market/about.html', context)
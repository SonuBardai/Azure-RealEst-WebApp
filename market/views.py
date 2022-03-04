from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'login' : False
    }
    return render(request, 'market/home.html', context)

def dashboard(request):
    context = {
        'login' : False
    }
    return render(request, 'market/dashboard.html', context)

def about(request):
    context = {
        'login' : False
    }
    return render(request, 'market/about.html', context)
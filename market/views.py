from django.shortcuts import render
from .models import Properties
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'login' : False
    }
    return render(request, 'market/home.html', context)

def dashboard(request):
    properties = Properties.objects.all().order_by('-listing_date')

    context = {
        'login' : False, 
        'properties' : properties,
    }
    return render(request, 'market/dashboard.html', context)

def about(request):
    context = {
        'login' : False
    }
    return render(request, 'market/about.html', context)

def contact(request):
    pass

class NewProperty(LoginRequiredMixin, CreateView):
    model = Properties
    fields = ['title', 'desc', 'size', 'bedrooms', 'price', 'image1', 'image2', 'image3']

    def form_valid(self, form):
        form.instance.listed_by = self.request.user
        return super().form_valid(form)

class UpdateProperty(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Properties
    fields = ['title', 'desc', 'size', 'bedrooms', 'price', 'image1', 'image2', 'image3']

    def test_func(self):
        property = self.get_object()
        return True if self.request.user == property.listed_by else False

class DeleteProperty(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Properties
    success_url = '/dashboard/'

    def test_func(self):
        property = self.get_object()
        return True if self.request.user == property.listed_by else False

class DetailProperty(DetailView):
    model = Properties
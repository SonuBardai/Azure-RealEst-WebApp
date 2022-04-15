from itertools import chain
from django.db import models
from django.shortcuts import redirect, render
from .models import Properties
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
import os
import json


def home(request):
    context = {
        'login': False
    }
    return render(request, 'market/home.html', context)


def dashboard(request):
    if request.method == 'POST' and request.POST['search']:
        queries = request.POST['search'].split(" ")
        
        properties = None
        for query in queries:
            if not query:
                continue
            properties = list(chain(Properties.objects.filter(
                models.Q(title__icontains=query) |
                models.Q(tags__icontains=query) |
                models.Q(desc__icontains=query) |
                models.Q(location__icontains=query)
            )))
        context = {
            'properties': properties,
            'filters': queries
        }
        return render(request, 'market/dashboard.html', context)

    properties = Properties.objects.all().order_by('-listing_date')

    context = {
        'login': False,
        'properties': properties,
    }
    return render(request, 'market/dashboard.html', context)


def about(request):
    context = {
        'login': False
    }
    return render(request, 'market/about.html', context)


class NewProperty(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Properties
    fields = ['title', 'desc', 'location', 'size',
              'bedrooms', 'price', 'image1', 'image2', 'image3']
    success_message = 'Property Listed'

    def form_valid(self, form):
        form.instance.listed_by = self.request.user
        return super().form_valid(form)


class UpdateProperty(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Properties
    fields = ['title', 'desc', 'location', 'size',
              'bedrooms', 'price', 'image1', 'image2', 'image3']
    success_message = 'Listing Updated'

    def test_func(self):
        property = self.get_object()
        return True if self.request.user == property.listed_by else False


class DeleteProperty(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Properties
    success_url = '/dashboard/'

    success_message = 'Property De-listed'

    def test_func(self):
        property = self.get_object()
        return True if self.request.user == property.listed_by else False

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        # Deleting images associated with the Delisted Property

        os.remove(instance.image1.path)
        # Deleting image1

        name_split = os.path.split(instance.image1.path)
        thumbnail_path = os.path.join(
            name_split[0], 'thumbnail-'+name_split[1])
        os.remove(thumbnail_path)
        # Deleting thumbnail of image1

        if instance.image2:
            os.remove(instance.image2.path)
        if instance.image3:
            os.remove(instance.image3.path)
        # Deleting image2 and image3

        # Displaying successfully deleted message
        messages.success(self.request, self.success_message)
        return super(DeleteProperty, self).delete(request, *args, **kwargs)


class DetailProperty(DetailView):
    model = Properties

    def get_context_data(self, *args, **kwargs):
        context = super(DetailProperty, self).get_context_data(*args, **kwargs)
        property = Properties.objects.filter(slug=self.kwargs['slug']).first()
        context['tags'] = json.loads(property.tags)
        return context

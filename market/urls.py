from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='market-home'),
    path('dashboard/', views.dashboard, name='market-dashboard'),
    path('about/', views.about, name='market-about'),
]
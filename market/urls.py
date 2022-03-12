from django.urls import path
from . import views
from .views import (
    NewProperty,
    UpdateProperty,
    DeleteProperty,
    DetailProperty
)

urlpatterns = [
    path('', views.home, name='market-home'),
    path('dashboard/', views.dashboard, name='market-dashboard'),
    path('about/', views.about, name='market-about'),
    path('property/new/', NewProperty.as_view(), name='property-new'),
    path('property/<str:slug>/update/', UpdateProperty.as_view(), name='property-update'),
    path('property/<str:slug>/delete/', DeleteProperty.as_view(), name='property-delete'),
    path('property/<str:slug>/detail/', DetailProperty.as_view(), name='property-detail'),
]
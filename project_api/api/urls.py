# api/urls.py
from django.urls import include
from django.urls import path

urlpatterns = [
    path('partners/', include('partners.urls')),
]

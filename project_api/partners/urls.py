# partners/urls.py
from django.urls import include
from django.urls import path

from .views import PartnerListView

urlpatterns = [
    path('', PartnerListView.as_view()),
]

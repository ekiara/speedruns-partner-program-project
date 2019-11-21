# partners/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Partner
from .serializers import PartnerSerializer


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerCreate(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerRetrieve(generics.RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerUpdate(generics.UpdateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDelete(generics.DestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

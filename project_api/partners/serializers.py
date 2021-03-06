# partners/serializers.py
from rest_framework import serializers
from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('id', 'name', 'program_count', )

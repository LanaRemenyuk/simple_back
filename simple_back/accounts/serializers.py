from rest_framework import serializers
from .models import CustomerProfile, ProviderProfile


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ('name', 'contact_data', 'specialty', 'info')


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = ('name', 'contact_data', 'specialty', 'info', 'experience_in_years')
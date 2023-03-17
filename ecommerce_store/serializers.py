from rest_framework import serializers
from .models import EcommerceStore

class EcommerceStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceStore
        fields = '__all__'
from ecommerce_store.serializers import EcommerceStoreSerializer
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    ecommerce_store = EcommerceStoreSerializer(many=True,read_only=True)
    class Meta:
        model: User
        fields = ['id','username','password','email','ecommerce_store']
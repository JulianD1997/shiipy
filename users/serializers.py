from ecommerce_store.serializers import EcommerceStoreSerializer
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    serializador para objetos de tipo User,añade un representacion para los objetos relacionados con EcommerceStore
    Atributos:
        eccomerce_stores (EcommerceStoreSerializer) = Un serializador anidado para representar los objetos relacionados 
            con el modelo EcommerceStore
        model(User): Modelo User el que se va a serializar
        fields (list): Los campos que se reprensentaran para la serializacion
    """
    ecommerce_stores = EcommerceStoreSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'ecommerce_stores']

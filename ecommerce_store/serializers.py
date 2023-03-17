from rest_framework import serializers
from .models import EcommerceStore


class EcommerceStoreSerializer(serializers.ModelSerializer):
    """
    serializador para objetos de tipo Ecommerce
    Atributos:
        model(EcommerceStore): Modelo EcommerceStore el cual se va a serializar
        fields (list): Los campos que se reprensentaran para la serializacion
    """
    class Meta:
        model = EcommerceStore
        fields = '__all__'

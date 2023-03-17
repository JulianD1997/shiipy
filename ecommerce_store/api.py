from rest_framework import generics
from .models import EcommerceStore
from .serializers import EcommerceStoreSerializer


class EcommerceStoreList(generics.ListCreateAPIView):
    """
    Esta clase sirve para manejar las solicitudes GET y POST
    para los objetos de tipo EcommerStore
    atributos:
        queryset (QuerySet): retorna todos los datos de EcommerceStore de la base de datos
        serializer_class (EcommerceStoreSerializer): serializar los objetos(json)
    """
    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreSerializer


class EcommerceStoreDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Esta clase sirve para manejar las solicitudes GET, PUT y DELETE
    para un objeto de tipo EcommerStore
    atributos:
        queryset (QuerySet): Obtencion de los datos del modelo EcommerceStore
        serializer_class (EcommerceStoreSerializer): serializar los objetos(json)
    """
    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreSerializer

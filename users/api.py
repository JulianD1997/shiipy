from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """
    Esta clase sirve para manejar las solicitudes GET y POST
    para los objetos de tipo User
    atributos:
        queryset (QuerySet): Obtencion de todos los datos de User
        serializer_class (EcommerceStoreSerializer): serializar los objetos(json)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Esta clase sirve para manejar las solicitudes GET, PUT y DELETE
    para un objeto de tipo User
    atributos:
        queryset (QuerySet): Obtencion de los datos del modelo User
        serializer_class (EcommerceStoreSerializer): serializar los objetos(json)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

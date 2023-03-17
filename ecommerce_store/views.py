from rest_framework import generics
from .models import EcommerceStore
from .serializers import EcommerceStoreSerializer

class EcommerceStoreList(generics.ListCreateAPIView):
    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreSerializer

class EcommerceStoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreSerializer

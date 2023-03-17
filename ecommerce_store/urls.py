from django.urls import path
from .api import EcommerceStoreList, EcommerceStoreDetail

"""
Rutas para ecommerce_store
"""
urlpatterns = [
    path('', EcommerceStoreList.as_view(), name='ecommerce_store-list'),
    path('<int:pk>', EcommerceStoreDetail.as_view(),
         name='ecommerce_store-detail'),
]

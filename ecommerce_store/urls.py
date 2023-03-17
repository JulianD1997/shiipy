from django.urls import path
from .views import EcommerceStoreList,EcommerceStoreDetail

urlpatterns = [
    path('',EcommerceStoreList.as_view(),name='ecommerce_store-list'),
    path('<int:pk>',EcommerceStoreDetail.as_view(),name='ecommerce_store-detail'),
]
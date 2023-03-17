from django.urls import path
from .api import UserList, UserDetail
"""
Rutas para usurios
"""
urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>', UserDetail.as_view(), name='user-detail'),
]

from django.contrib import admin
from django.urls import path, include
"""
Ruta directas del proyecto
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('ecommerce_store/', include('ecommerce_store.urls')),
]

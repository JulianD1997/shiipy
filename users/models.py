from django.db import models
from ecommerce_store.models import EcommerceStore
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    ecommerce_store = models.ForeignKey(EcommerceStore, on_delete=models.CASCADE, related_name='users')
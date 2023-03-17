from users.models import User
from django.db import models

class EcommerceStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
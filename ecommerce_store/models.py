from users.models import User
from django.db import models


class EcommerceStore(models.Model):
    """
    Este clase representa un modelo de tienda

    atributos:
        name (str): nombre de la tienda, no puede ser nulo
        location(str): Localizacion de la tienda (pais)
        user(User): usario asociado a la tienda
    """
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)

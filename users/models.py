from django.db import models
# Create your models here.


class User(models.Model):
    """
    Este clase representa un modelo usuario

    atributos:
        username (str): username del usuario, no puede ser nulo y debe ser unico
        password (str): password del usuario, no pueder ser nulo
        email (str): email del userio, no puede ser nulo y debe ser unico
    """
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)

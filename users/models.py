from django.db import models
# Create your models here.

class User(models.Model):
    """
    A model representing a user account.

    Attributes:
        username (str): The username for the user account.
        password (str): The password for the user account.
        email (str): The email address for the user account.
    """
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    
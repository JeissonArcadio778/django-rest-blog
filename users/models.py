from django.contrib.auth.models import AbstractUser
from django.db import models 

# añadir nuevas caracteristicas al usuario, panel
class User(AbstractUser):
    web_site = models.CharField(max_length=255, blank=True)
    Twitter = models.CharField(max_length=255, blank=True)

    # use email for login
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



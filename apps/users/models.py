from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass
    rol = models.IntegerField(default=0)
    direccion = models.CharField(max_length=250, null=True)
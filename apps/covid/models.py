from django.db import models
from apps.users.models import User
class Doctor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
class Labatorista(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
class MINSAL(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
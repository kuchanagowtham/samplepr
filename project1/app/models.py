from django.db import models

# Create your models here.
class Myregistration(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(unique=True,max_length=100)
	password = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	email = models.CharField(max_length=100,unique=True)
	adress = models.CharField(max_length=100)

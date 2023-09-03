from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField()

class Remera(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=40)
    talle = models.CharField(max_length=3)

class Taza(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=40)
from django.db import models

# Create your models here.

class Perro(models.Model):
    
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()
    esCastrado = models.BooleanField()


class Pajaro(models.Model):

    especie = models.CharField(max_length=40)
    zona = models.CharField(max_length=40)
    esExotico = models.BooleanField(null=True)

class Pez(models.Model):

    especie = models.CharField(max_length=40)
    deAguaSalada = models.BooleanField(null=True)
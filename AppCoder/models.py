from django.db import models
from django import forms

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=40) #campo de texto
    comision= models.IntegerField() #campo de enteros

class Estudiante(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    emails= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    emails= models.EmailField()
    profesion= models.CharField(max_length=40)

class Entregable (models.Model):
    nombre= models.CharField(max_length=40)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()
    


from django.db import models
from django import forms

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=40) #campo de texto
    comision= models.IntegerField() #campo de enteros

    def __str__(self):
        return self.nombre+"  "+str(self.comision)

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
    

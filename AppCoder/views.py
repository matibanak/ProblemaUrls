from django.http import HttpResponse
from django.shortcuts import render
from .models import *
def curso(self):

    curso= Curso(nombre="Django", comision=939393)
    curso.save()
    texto= f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

# Create your views here.
def inicio(request):
    return render (request, '.AppCoder.inicio.html')

def cursos(request):
    return render(request, "Appcoder/cursos.html")

def profesores(request):
    return render (request, "Appcoder/profesores.html")

def estudiantes(request):
    return render (request, "Appcoder/estudiantes.html")

def entregables(request):
    return render (request, "Appcoder/entregables.html")

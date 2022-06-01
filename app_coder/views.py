from django.shortcuts import render
from app_coder.models import Curso
from app_coder.models import Estudiante
from app_coder.models import Profesor
from django.http import HttpResponse
# Create your views here.

def cursos(request):
    return render(request, "app_coder/cursos.html")

def estudiantes(request):
    return render(request, "app_coder/estudiantes.html")

def profesor(request):
    return render(request, "app_coder/profesor.html")

def inicio(request):
    return render(request, "app_coder/index.html")
from django.urls import path
from app_coder import views


urlpatterns = [
    path('inicio', views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('estudiantes', views.estudiantes),
    path('profesor', views.profesor),
]
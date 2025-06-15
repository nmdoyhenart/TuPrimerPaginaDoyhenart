from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('agregar_genero/', views.agregar_genero, name='agregar_genero'),
    path('agregar_director/', views.agregar_director, name='agregar_director'),
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),
]
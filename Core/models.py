from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre_completo = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    anio = models.PositiveIntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Profile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/',              
        default='avatars/default.png',     
        blank=True, null=True
    )
    bio    = models.TextField(blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
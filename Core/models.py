from django.db import models

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

    def __str__(self):
        return self.titulo
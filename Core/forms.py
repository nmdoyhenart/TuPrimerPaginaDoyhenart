from django import forms
from .models import Pelicula, Genero, Director

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['nombre_completo', 'nacionalidad']
from django.shortcuts import render, redirect
from .forms import PeliculaForm, GeneroForm, DirectorForm
from .models import Pelicula

def home(request):
    return render(request, 'Core/home.html')

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'Core/inicio.html', {'peliculas': peliculas})

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigí a la página principal u otra
    else:
        form = PeliculaForm()
    return render(request, 'Core/agregar_pelicula.html', {'form': form})

def agregar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GeneroForm()
    return render(request, 'Core/agregar_genero.html', {'form': form})

def agregar_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DirectorForm()
    return render(request, 'Core/agregar_director.html', {'form': form})

def buscar_pelicula(request):
    query = request.GET.get('query', '')
    peliculas = Pelicula.objects.filter(titulo__icontains=query) if query else []

    return render(request, 'Core/buscar.html', {
        'query': query,
        'peliculas': peliculas
    })
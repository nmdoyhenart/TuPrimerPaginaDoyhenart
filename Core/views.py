from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import PeliculaForm, GeneroForm, DirectorForm
from .models import Pelicula
from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm

def home(request):
    return render(request, 'Core/home.html')

def inicio(request):
    return render(request, "Core/inicio.html")

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, "Core/inicio.html", {"peliculas": peliculas})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)                 # logueo automático
            messages.success(request, "¡Tu cuenta fue creada!")
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "Core/registration/signup.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Perfil actualizado")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "Core/profile.html", context)

@login_required
def editar_pelicula(request, pk):
    peli = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=peli)
        if form.is_valid():
            form.save()
            return redirect('detalle_pelicula', pk=peli.pk)
    else:
        form = PeliculaForm(instance=peli)
    return render(request, 'Core/editar_pelicula.html', {'form': form, 'peli': peli})

@login_required
def eliminar_pelicula(request, pk):
    peli = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        peli.delete()
        return redirect('inicio')
    return render(request, 'Core/eliminar_pelicula.html', {'peli': peli})

def agregar_pelicula(request):
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PeliculaForm()
    return render(request, "Core/agregar_pelicula.html", {"form": form})

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

def detalle_pelicula(request, pk):
    peli = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'Core/detalle_pelicula.html', {'peli': peli})
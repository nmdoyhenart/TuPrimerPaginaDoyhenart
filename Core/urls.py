from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Listado/detalle
    path('', views.home, name='home'),
    path('pages/', views.index, name='index'), 
    path('inicio/', views.inicio, name='inicio'),

    # Auth
    path('login/', auth_views.LoginView.as_view(
        template_name='Core/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Perfil
    path('profile/', views.profile, name='profile'),

    # Agregar
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('agregar_genero/', views.agregar_genero, name='agregar_genero'),
    path('agregar_director/', views.agregar_director, name='agregar_director'),

    # Buscar
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),
    path('buscar/', views.buscar_pelicula, name='buscar_pelicula'),

    # Vista
    path('pages/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('pages/<int:pk>/editar/', views.editar_pelicula, name='editar_pelicula'),
    path('pages/<int:pk>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),
]
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pelicula, Genero, Director, Profile

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

# Registros
class Registro(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # aseguramos que el email sea único
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ese correo ya está registrado.")
        return email
    
class UserCreationForm(UserCreationForm):
    email  = forms.EmailField(required=True, label="Correo")
    avatar = forms.ImageField(required=False, label="Foto de perfil")

    class Meta:
        model  = User
        fields = ("username", "email", "avatar", "password1", "password2")

    # guardamos el avatar en Profile
    def save(self, commit=True):
        user = super().save(commit)
        avatar = self.cleaned_data.get("avatar")
        if avatar:
            user.profile.avatar = avatar
            if commit:
                user.profile.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Correo")

    class Meta:
        model  = User
        fields = ("username", "email")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ("avatar", "bio")
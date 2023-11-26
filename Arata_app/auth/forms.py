from django import forms
from django.contrib.auth.forms import UserCreationForm
from .usuario import Usuario

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password1', 'password2']
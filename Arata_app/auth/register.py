from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UsuarioRegistroForm

def registro(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión después del registro
            return redirect('inicio')  # Cambia 'inicio' al nombre de tu vista de inicio
    else:
        form = UsuarioRegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})
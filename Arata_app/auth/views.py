from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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

def login(request):
    return render(request, 'auth/login.html', {})

def loginAuth(request):
    user_name = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request,user)
        return redirect('dashboard')
    else:
        print(user_name,password)
        return redirect('login')
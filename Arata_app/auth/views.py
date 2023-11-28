from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Reemplaza 'home' con la URL a la que deseas redirigir después del login
        else:
            return render(request, self.template_name, {'error_message': 'Invalid login credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Reemplaza 'login' con la URL a la que deseas redirigir después del logout

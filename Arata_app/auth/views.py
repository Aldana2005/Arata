from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
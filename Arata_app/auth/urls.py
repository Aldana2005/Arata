from django.urls import path
from . import views

urlpatterns = [
    # Registro
    path('registro/', views.registro, name='registro'),
    path('login/', views.login , name='login'),
    path('loginAuth/', views.loginAuth, name='loginAuth'),
]

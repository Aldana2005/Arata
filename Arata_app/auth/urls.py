from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Otras URLS...

    # Registro
    path('registro/', views.registro, name='registro'),

    # Inicio de sesión
    path('inicio_sesion/', auth_views.LoginView.as_view(template_name='usuarios/inicio_sesion.html'), name='inicio_sesion'),

    # Cierre de sesión
    path('cerrar_sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),
]

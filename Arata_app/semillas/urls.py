from django.urls import path
from . import views

urlpatterns = [
    path('semillas/', views.lista_semillas, name='lista_semillas'),
    path('semillas/<int:pk>/', views.detalle_semilla, name='detalle_semilla'),
    path('semillas/nueva/', views.agregar_semilla, name='agregar_semilla'),
    path('semillas/editar/<int:pk>/', views.editar_semilla, name='editar_semilla'),
    path('semillas/eliminar/<int:pk>/', views.eliminar_semilla, name='eliminar_semilla'),
]
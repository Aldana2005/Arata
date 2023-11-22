from django.urls import path
from . import views

urlpatterns = [
    path('semillas/', views.semilla_list, name='semilla_list'),
    path('semilla/<int:pk>/', views.semilla_detail, name='semilla_detail'),
    path('semilla/new/', views.semilla_new, name='semilla_new'),
    path('semilla/<int:pk>/edit/', views.semilla_edit, name='semilla_edit'),
    path('semilla/<int:pk>/delete/', views.semilla_delete, name='semilla_delete'),
    path('ubicacion/new/', views.ubicacion_new, name='ubicacion_new'),
]
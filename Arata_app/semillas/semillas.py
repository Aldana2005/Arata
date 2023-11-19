from django.db import models

class Semilla(models.Model):
    nombre = models.CharField(max_length=100)
    variedad = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    caracteristicas = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.nombre

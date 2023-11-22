from django.db import models

class Semilla(models.Model):
    nombre = models.CharField(max_length=100)
    variedad = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    caracteristicas = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    ubicacion = models.OneToOneField('Ubicacion', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    horario = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    
    def __str__(self):
        return self.contacto
from django import forms
from .seed import Semilla, Ubicacion

class SemillaForm(forms.ModelForm):

    class Meta:
        model = Semilla
        fields = ('nombre', 'variedad', 'origen', 'caracteristicas', 'precio', 'cantidad_disponible', 'ubicacion')

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ('latitud', 'longitud', 'horario', 'contacto')
from django.shortcuts import render, get_object_or_404, redirect
from .models import Semilla
from .forms import SemillaForm  # Asegúrate de crear un formulario (forms.py) para la entrada de datos

def lista_semillas(request):
    semillas = Semilla.objects.all()
    return render(request, 'semillas/lista_semillas.html', {'semillas': semillas})

def detalle_semilla(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
    return render(request, 'semillas/detalle_semilla.html', {'semilla': semilla})

def agregar_semilla(request):
    if request.method == "POST":
        form = SemillaForm(request.POST)
        if form.is_valid():
            semilla = form.save(commit=False)
            semilla.save()
            return redirect('detalle_semilla', pk=semilla.pk)
    else:
        form = SemillaForm()
    return render(request, 'semillas/editar_semilla.html', {'form': form})

def editar_semilla(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
    if request.method == "POST":
        form = SemillaForm(request.POST, instance=semilla)
        if form.is_valid():
            semilla = form.save(commit=False)
            semilla.save()
            return redirect('detalle_semilla', pk=semilla.pk)
    else:
        form = SemillaForm(instance=semilla)
    return render(request, 'semillas/editar_semilla.html', {'form': form})

def eliminar_semilla(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
    semilla.delete()
    return redirect('lista_semillas')
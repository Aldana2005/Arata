from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .seed import Semilla, Ubicacion
from .forms import SemillaForm, UbicacionForm

def home(request):
    return render(request, 'semillas/base_semilla.html', {})

def semilla_list(request):
    semillas = Semilla.objects.all()

    # Configurar paginación
    paginator = Paginator(semillas, 10)  # Mostrar 10 semillas por página
    page = request.GET.get('page')

    try:
        semillas_paginadas = paginator.page(page)
    except PageNotAnInteger:
        semillas_paginadas = paginator.page(1)
    except EmptyPage:
        semillas_paginadas = paginator.page(paginator.num_pages)

    return render(request, 'semillas/semilla_list.html', {'semillas': semillas_paginadas})

def semilla_detail(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
    return render(request, 'semillas/semilla_detail.html', {'semilla': semilla})

def semilla_new(request):
    if request.method == "POST":
        form = SemillaForm(request.POST)
        if form.is_valid():
            semilla = form.save(commit=False)
            semilla.save()
            return redirect('semilla_detail', pk=semilla.pk)
    else:
        form = SemillaForm()
    return render(request, 'semillas/semilla_edit.html', {'form': form})

def semilla_edit(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
    ubicaciones = Ubicacion.objects.all()

    if request.method == "POST":
        form = SemillaForm(request.POST, instance=semilla)
        if form.is_valid():
            semilla = form.save(commit=False)
            semilla.save()
            return redirect('semilla_detail', pk=semilla.pk)
    else:
        form = SemillaForm(instance=semilla)

    return render(request, 'semillas/semilla_edit.html', {'form': form, 'ubicaciones': ubicaciones})

def semilla_delete(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
    semilla.delete()
    return redirect('semillas/semilla_list')

def ubicacion_new(request):
    if request.method == "POST":
        form = UbicacionForm(request.POST)
        if form.is_valid():
            ubicacion = form.save()
            return redirect('semilla_new')
    else:
        form = UbicacionForm()
    return render(request, 'semillas/ubicacion_edit.html', {'form': form})
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import FormularioTerapia
from .models import Hora
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'paciente/index.html', {})

@login_required
def lista_terapia(request):
    return render(request, 'paciente/lista_terapia.html', {})

@login_required
def terapia(request):
    return render(request, 'paciente/terapia.html', {})

@login_required
def nueva_terapia(request):
    if request.method == "POST":
        formTera = FormularioTerapia(data=request.POST)
        if formTera.is_valid():
            terapia = formTera.save(commit=False)
            terapia.paciente = request.user
            terapia.save()
            return redirect('confirmacion_terapia', pk=terapia.pk)
        else:
            return render(request, 'paciente/nueva_terapia.html', {'formTera': formTera})
    else:
        formTera = FormularioTerapia()
        return render(request, 'paciente/nueva_terapia.html', {'formTera': formTera})

@login_required
def confirmacion_terapia(request, pk):
    terapia = get_object_or_404(Hora, pk=pk)
    return render(request, 'paciente/confirmacion_terapia.html', {'terapia': terapia})

@login_required
def terapia_detalle(request, pk):
    terapia = get_object_or_404(Hora, pk=pk)
    return render(request, 'paciente/terapia_detalle.html', {'terapia': terapia})

@login_required
def lista_terapia(request):
    terapia = Hora.objects.filter(fecha_atencion__gte=timezone.now()).order_by('fecha_atencion')
    return render(request, 'paciente/lista_terapia.html', {'terapia': terapia})

@login_required
def terapia_anterior(request):
    terapia = Hora.objects.filter(fecha_atencion__lte=timezone.now()).order_by('-fecha_atencion')
    return render(request, 'paciente/terapia_anterior.html', {'terapia': terapia})

@login_required
def eliminar_terapia(request, pk):
    terapia = Hora.objects.get(pk=pk)

    try:
        terapia.delete()
        mensaje = "Terapia cancelada"
        messages.success(request, mensaje)
    except:
        mensaje = "TNo se ha podido eliminar terapia"
        messages.error(request, mensaje)
    
    return redirect('lista_terapia')

@login_required
def menu(request):
    return render(request, 'paciente/menu.html', {})

@login_required
def menu_confirmacion(request):
    return render(request, 'paciente/menu_confirmacion.html', {})

@login_required
def campana(request):
    return render(request, 'paciente/campana.html', {})

@login_required
def campana_confirmacion(request):
    return render(request, 'paciente/campana_confirmacion.html', {})

@login_required
def emergencia(request):
    return render(request, 'paciente/emergencia.html', {})

@login_required
def transporte(request):
    return render(request, 'paciente/transporte.html', {})

@login_required
def transporte_confirmacion(request):
    return render(request, 'paciente/transporte_confirmacion.html', {})

@login_required
def contacto(request):
    return render(request, 'paciente/contacto.html', {})
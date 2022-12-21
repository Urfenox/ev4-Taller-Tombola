from django.shortcuts import render

from Tombola import forms as Formulario
from Tombola import models as Modelo

# Create your views here.

def index(request):
    return render(request, 'Inicio/index.html')

def registro(request):
    form = Formulario.FormRegistro()
    if request.method == 'POST':
        form = Formulario.FormRegistro(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Inicio/registro.html', data)

def solicitudes(request):
    form = Formulario.FormSolicitudes()
    if request.method == 'POST':
        form = Formulario.FormSolicitudes(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Inicio/solicitudes.html', data)

def contacto(request):
    return render(request, 'Inicio/contacto.html')

def resultados(request):
    ganadores = Modelo.Ganadores.objects.all()
    if request.method == 'POST':
        rutBuscado = request.POST['rut']
        ganadoresActuales = Modelo.Ganadores.objects.all()
        ganadores = []
        for item in ganadoresActuales:
            ganadores.append(item.rut)
        if int(rutBuscado) in ganadores:
            cupo = "Si"
        else:
            cupo = "No"
        resultado = {"rut": rutBuscado, "cupo": cupo}
        data = {"resultado": resultado}
    else:
        data = {"ganadores": ganadores}
    return render(request, 'Inicio/resultados.html', data)

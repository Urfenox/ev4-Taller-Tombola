from django.shortcuts import render, redirect

from .models import Registro, Solicitudes, ListaNegra, Ganadores

import random

# Create your views here.

def index(request, error = None):
    ganadores = Ganadores.objects.all()
    data = {"ganadores": ganadores, "error": error}
    return render(request, 'Tombola/index.html', data)

def panel(request):
    registrados = Registro.objects.all()
    solicitudes = Solicitudes.objects.all()
    data = {"registrados": registrados,
    "solicitudes": solicitudes}
    return render(request, 'Tombola/panel.html', data)


# Acciones de los botones de /panel/
def Realizar_Sorteo(request):
    cupos = 5
    # algoritmo. de los registro de solicitud,
    # ir seleccionando ganadores y
    # agregalos a la tabla Ganadores
    solicitantes = Solicitudes.objects.all()
    ganadoresActuales = Ganadores.objects.all()
    ganadores = []
    if (solicitantes.count() < 1):
        return index(request, error = {"mensaje": "No se puede realizar el sorteo con menos de una solicitud."})
    for item in ganadoresActuales:
        ganadores.append(item.rut)
    while (cupos>0):
        numero = random.randrange(0, solicitantes.count() - 1)
        ganador = solicitantes[numero]
        if ganador.rut in ganadores:
            print(ganador.rut + " no existe en Ganadores")
        else:
            registro = Ganadores(rut = ganador.rut, faltas = 0, estacionado = False)
            registro.save()
            cupos -= 1
    return redirect("../")

def Nuevo_Sorteo(request):
    # limpia la tabla ganadores
    # limpia la tabla solicitudes (?*)
    Ganadores.objects.all().delete()
    # Solicitudes.objects.all().delete()
    return redirect("../")

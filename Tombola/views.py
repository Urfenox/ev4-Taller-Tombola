from django.shortcuts import render, redirect

from .models import Registro, Solicitudes, ListaNegra, Ganadores

import random

# Create your views here.

def index(request):
    ganadores = Ganadores.objects.all()
    data = {"ganadores": ganadores}
    return render(request, 'Tombola/index.html', data)

def panel(request):
    return render(request, 'Tombola/panel.html')


# Acciones de los botones de /panel/
def Realizar_Sorteo(request):
    cupos = 5
    # algoritmo. de los registro de solicitud,
    # ir seleccionando ganadores y
    # agregalos a la tabla Ganadores
    solicitantes = Solicitudes.objects.all()
    ganadoresActuales = Ganadores.objects.all()
    ganadores = []
    for item in ganadoresActuales:
        ganadores.append(item.rut)
    while (cupos>0):
        numero = random.randrange(0, solicitantes.count() - 1)
        ganador = solicitantes[numero]
        # TODO: verificar que no exista ya en Ganadores
        # if (Ganadores.objects.filter(rut=ganador).exists() == False): # no existe # no funciona (error)
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

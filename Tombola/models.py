from django.db import models

# Create your models here.

def AutoIncrementar_Solicitudes():
    cantidad = Solicitudes.objects.count() + 1
    return cantidad

def AutoIncrementar_Registro():
    cantidad = Registro.objects.count() + 1
    return cantidad

def AutoIncrementar_ListaNegra():
    cantidad = ListaNegra.objects.count() + 1
    return cantidad

def AutoIncrementar_Ganadores():
    cantidad = Ganadores.objects.count() + 1
    return cantidad

# Solicitud de cada registro (el registro puede existir, pero si no hace una solicitud, no participara en e sorteo)
class Solicitudes(models.Model):
    id = models.AutoField(primary_key=True, default=AutoIncrementar_Solicitudes)
    rut = models.IntegerField()

# Registros de cada persona
class Registro(models.Model):
    id = models.AutoField(primary_key=True, default=AutoIncrementar_Registro)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.CharField(max_length=200)
    patente = models.CharField(max_length=10)
    licencia = models.CharField(max_length=50)

# Ruts en esta tabla no pueden hacer ni registros ni solicitudes ni ganar un cupo
class ListaNegra(models.Model):
    id = models.AutoField(primary_key=True, default=AutoIncrementar_ListaNegra)
    rut = models.IntegerField()
    fechaFalta = models.DateField()

# Los ruts de aqui son los que han ganado un cupo para el uso del estacionamiento
class Ganadores(models.Model):
    id = models.AutoField(primary_key=True, default=AutoIncrementar_Ganadores)
    rut = models.IntegerField()
    faltas = models.IntegerField()
    estacionado = models.BooleanField()

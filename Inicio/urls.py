from django.urls import path

from . import views as app

urlpatterns = [
    path('', app.index),
    path('contacto/', app.contacto, name="contacto"),
    path('registro/', app.registro, name="registro"),
    path('solicitudes/', app.solicitudes, name="solicitudes"),
    path('resultados/', app.resultados, name="resultados")
]

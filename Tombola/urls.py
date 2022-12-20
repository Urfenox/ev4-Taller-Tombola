from django.urls import path

from . import views as app

urlpatterns = [
    path('', app.index),
    path('panel/', app.panel),
    path('do_sorteo/', app.Realizar_Sorteo, name='do_sorteo'),
    path('new_sorteo/', app.Nuevo_Sorteo, name='new_sorteo')
]

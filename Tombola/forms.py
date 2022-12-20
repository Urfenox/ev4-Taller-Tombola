from django import forms
from . import models as modelo

class FormRegistro(forms.ModelForm):
    class Meta:
        model = modelo.Registro
        fields = '__all__'

class FormSolicitudes(forms.ModelForm):
    class Meta:
        model = modelo.Solicitudes
        fields = '__all__'

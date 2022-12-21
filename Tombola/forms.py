from django import forms
from . import models as modelo

class FormRegistro(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormRegistro, self).__init__(*args, **kwargs)
        self.fields['rut'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['patente'].widget.attrs['class'] = 'form-control'
        self.fields['licencia'].widget.attrs['class'] = 'form-control'

        self.fields['rut'].widget.attrs['placeholder'] = 'Sin puntos ni guion. Si termina en K poner 0'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre y Apellido'
        self.fields['telefono'].widget.attrs['placeholder'] = '9XXXXXXXXX'
        self.fields['email'].widget.attrs['placeholder'] = 'nombre@example.com'
        self.fields['patente'].widget.attrs['placeholder'] = 'ABCD00'
        self.fields['licencia'].widget.attrs['placeholder'] = 'Número de licencia'

    class Meta:
        model = modelo.Registro
        fields = '__all__'

class FormSolicitudes(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSolicitudes, self).__init__(*args, **kwargs)
        self.fields['rut'].widget.attrs['class'] = 'form-control'

        self.fields['rut'].widget.attrs['placeholder'] = 'Sin puntos ni guion. Si termina en K poner 0'

    class Meta:
        model = modelo.Solicitudes
        fields = '__all__'


# https://stackoverflow.com/questions/8474409/django-forms-and-bootstrap-css-classes-and-divs
# https://stackoverflow.com/questions/3168939/django-modelform-and-css-styling
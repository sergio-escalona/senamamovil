from django import forms
from .models import Hora, Terapeuta

class FormularioTerapia(forms.ModelForm):

    fecha_atencion = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Hora
        fields = ('terapeuta', 'fecha_atencion',)

class FormularioTerapeuta(forms.ModelForm):
    class Meta:
        model = Terapeuta
        fields = ('terapeuta', 'rut',)
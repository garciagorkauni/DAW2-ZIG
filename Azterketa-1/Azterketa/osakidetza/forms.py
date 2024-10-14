from django import forms
from .models import Pazientea, Medikua

class PazienteaForm(forms.ModelForm):
    class Meta:
        model=Pazientea
        fields=['izena','abizena','telefonoa']

class MedikuaForm(forms.ModelForm):
    class Meta:
        model=Medikua
        fields=['izena','abizena','espezialidadea']
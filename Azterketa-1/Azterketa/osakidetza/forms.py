from django import forms
from .models import Pazientea, Medikua, Zita

class PazienteaForm(forms.ModelForm):
    class Meta:
        model=Pazientea
        fields=['izena','abizena','telefonoa']

class MedikuaForm(forms.ModelForm):
    class Meta:
        model=Medikua
        fields=['izena','abizena','espezialidadea']

class ZitaForm(forms.ModelForm):
    class Meta:
        model=Zita
        fields=['data','oharra','pazientea', 'medikua']
from django import forms
from .models import Ikasle, Nota, Ikasgaia

class IkasleForm(forms.ModelForm):
    class Meta:
        model=Ikasle
        fields=['izena','abizena','jaiotze_data']

class IkasgaiForm(forms.ModelForm):
    class Meta:
        model=Ikasgaia
        fields=['izena','maila', 'hizkuntza']

class NotaForm(forms.ModelForm):
    class Meta:
        model=Nota
        fields=['ikasle','ikasgaia', 'nota', 'oharra']
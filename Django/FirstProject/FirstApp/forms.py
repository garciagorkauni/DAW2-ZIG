from django import forms
from .models import Ikasle

class IkasleForm(forms.ModelForm):
    class Meta:
        model=Ikasle
        fields=['izena','abizena','jaiotze_data']
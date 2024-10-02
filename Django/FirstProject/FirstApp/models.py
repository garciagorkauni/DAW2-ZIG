from django.db import models
from django.utils import timezone

# Create your models here.
class Ikasle(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    jaiotze_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.izena} {self.abizena} ({self.jaiotze_data})"

class Ikasgaia(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    maila = models.CharField(max_length=100)
    hizkuntza = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.izena} (Maila: {self.maila} - Hizkuntza: {self.hizkuntza})"

class Nota(models.Model):
    nota = models.FloatField()
    oharra = models.CharField(max_length=100)
    ikasgaia = models.ForeignKey(Ikasgaia, to_field='id', on_delete=models.CASCADE)
    ikasle = models.ForeignKey(Ikasle, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ikasle.izena} - {self.ikasgaia.izena}: {self.nota} ({self.oharra})"
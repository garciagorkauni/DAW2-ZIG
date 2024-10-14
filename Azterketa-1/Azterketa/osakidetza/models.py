from django.db import models
from django.utils import timezone

class Pazientea(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=75)
    telefonoa = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.izena} {self.abizena} ({self.telefonoa})"

class Medikua(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=75)
    espezialidadea = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.izena} {self.abizena} ({self.espezialidadea})"

class Zita(models.Model):
    data = models.DateTimeField(default=timezone.now)
    oharra = models.CharField(max_length=200)
    pazientea = models.ForeignKey(Pazientea, on_delete=models.CASCADE)
    medikua = models.ForeignKey(Medikua, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pazientea.izena} ({self.data}): {self.oharra}"

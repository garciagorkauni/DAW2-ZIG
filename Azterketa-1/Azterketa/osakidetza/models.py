from django.db import models

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

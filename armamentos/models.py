from django.db import models

class Armamento(models.Model):
    modelo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50, unique=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.modelo} ({self.numero_serie})"
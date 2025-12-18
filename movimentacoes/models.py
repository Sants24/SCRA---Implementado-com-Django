from django.db import models
from armamentos.models import Armamento
from django.conf import settings

class Movimentacao(models.Model):
    armamento = models.ForeignKey(Armamento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    TIPO_CHOICES = (
        ('RESERVA', 'Reserva'),
        ('RETIRADA', 'Retirada'),
        ('DEVOLUCAO', 'Devolução'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.armamento}"
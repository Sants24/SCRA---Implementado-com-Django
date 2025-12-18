from django.db import models
from armamentos.models import Armamento

class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('SAIDA', 'Cautela (Saída)'),
        ('ENTRADA', 'Devolução (Entrada)'),
    ]
    

    armamento = models.ForeignKey(Armamento, on_delete=models.CASCADE)
    tipo_movimentacao = models.CharField(max_length=10, choices=TIPO_CHOICES)
    responsavel = models.CharField(max_length=100) 
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_movimentacao} - {self.armamento.modelo}"
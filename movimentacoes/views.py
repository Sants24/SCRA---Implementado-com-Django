from django.shortcuts import render
from .models import Movimentacao

def consultar_historico(request):
   
    movimentacoes = Movimentacao.objects.all().order_by('-data_registro')
    return render(request, 'movimentacoes/historico.html', {'movimentacoes': movimentacoes})
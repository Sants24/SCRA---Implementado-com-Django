from django.shortcuts import render, redirect, get_object_or_404
from .models import Movimentacao
from armamentos.models import Armamento

def consultar_historico(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data_registro')
    return render(request, 'movimentacoes/historico.html', {'movimentacoes': movimentacoes})

def registrar_movimentacao(request):
    armamentos = Armamento.objects.all()
    mensagem_erro = None 

    if request.method == "POST":
        armamento_id = request.POST.get('armamento')
        tipo_movimentacao = request.POST.get('tipo') 
        responsavel = request.POST.get('responsavel')

        arma = get_object_or_404(Armamento, pk=armamento_id)
        
        
        if tipo_movimentacao == 'SAIDA' and not arma.disponivel:
            mensagem_erro = f"ERRO: A arma {arma.modelo} já consta como emprestada! Faça a devolução antes."
            
        
        elif tipo_movimentacao == 'ENTRADA' and arma.disponivel:
            mensagem_erro = f"ERRO: A arma {arma.modelo} já está no estoque. Verifique se selecionou a arma correta."
            
        else:
            
            Movimentacao.objects.create(
                armamento=arma,
                tipo_movimentacao=tipo_movimentacao,
                responsavel=responsavel
            )

            
            if tipo_movimentacao == 'SAIDA':
                arma.disponivel = False
            elif tipo_movimentacao == 'ENTRADA':
                arma.disponivel = True
            
            arma.save()
            return redirect('consultar_historico')


    return render(request, 'movimentacoes/form_movimentacao.html', {
        'armamentos': armamentos, 
        'erro': mensagem_erro
    })
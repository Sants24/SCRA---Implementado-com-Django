from django.shortcuts import render, redirect, get_object_or_404
from .models import Armamento
from .forms import ArmamentoForm

# UC04 - Listar Armamentos
def listar_armamentos(request):
    armamentos = Armamento.objects.all()
    return render(request, 'armamentos/listar_armamentos.html', {'armamentos': armamentos})

# UC03 - Adicionar Armamento (Esta era a função que faltava)
def adicionar_armamento(request):
    if request.method == 'POST':
        form = ArmamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_armamentos')
    else:
        form = ArmamentoForm()
    return render(request, 'armamentos/armamento_form.html', {'form': form})

def detalhes_armamento(request, pk):
    armamento = get_object_or_404(Armamento, pk=pk)
    return render(request, 'armamentos/detalhes_armamento.html', {'produto': armamento})

def excluir_armamento(request, pk):
    armamento = get_object_or_404(Armamento, pk=pk)
    armamento.delete()
    return redirect('listar_armamentos')
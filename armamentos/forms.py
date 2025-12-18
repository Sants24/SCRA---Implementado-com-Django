from django import forms 
from .models import Armamento

class ArmamentoForm(forms.ModelForm):
    class Meta:
        model = Armamento
        fields = ['modelo', 'tipo', 'numero_serie', 'disponivel']
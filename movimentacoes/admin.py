from django.contrib import admin
from .models import Movimentacao

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    # Agora 'data_registro' existe no model
    list_display = ('armamento', 'usuario', 'tipo', 'data_registro')
    list_filter = ('tipo', 'data_registro')
    readonly_fields = ('data_registro',) 
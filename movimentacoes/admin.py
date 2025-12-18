from django.contrib import admin
from .models import Movimentacao

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('armamento', 'tipo_movimentacao', 'responsavel', 'data_registro')
    list_filter = ('tipo_movimentacao', 'data_registro')
    search_fields = ('responsavel', 'armamento__modelo')
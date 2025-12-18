from django.contrib import admin
from .models import Armamento

@admin.register(Armamento)
class ArmamentoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'tipo', 'numero_serie', 'disponivel')
    list_filter = ('tipo', 'disponivel')
    search_fields = ('numero_serie', 'modelo')
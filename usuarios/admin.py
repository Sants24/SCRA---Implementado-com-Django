# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Adiciona os campos personalizados de Perfil e Matrícula no painel
    fieldsets = UserAdmin.fieldsets + (
        ('Informações do SCRA', {'fields': ('perfil', 'matricula')}),
    )
    list_display = ('username', 'email', 'perfil', 'is_staff')
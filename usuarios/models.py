from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PERFIS = (
        ('ADMIN', 'Administrador'),
        ('ARMEIRO', 'Armeiro'),
    )
    perfil = models.CharField(max_length=10, choices=PERFIS, default='ARMEIRO')
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
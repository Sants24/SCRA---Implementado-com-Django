from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_armamentos, name='listar_armamentos'),
    path('novo/', views.adicionar_armamento, name='adicionar_armamento'), 
    path('detalhes/<int:pk>/', views.detalhes_armamento, name='detalhes_armamento'),
    path('excluir/<int:pk>/', views.excluir_armamento, name='excluir_armamento'),
]
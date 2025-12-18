from django.urls import path
from .views import RealizarLogin, RealizarLogout

urlpatterns = [
    path('login/', RealizarLogin.as_view(), name='login'),
    path('logout/', RealizarLogout.as_view(), name='logout'),
]
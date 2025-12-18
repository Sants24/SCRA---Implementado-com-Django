from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class RealizarLogin(LoginView):
    template_name = 'usuarios/login.html' 

class RealizarLogout(LogoutView):
    next_page = reverse_lazy('login')
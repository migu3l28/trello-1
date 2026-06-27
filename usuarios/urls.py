# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crud/', views.leer_usuarios, name='leer_usuarios'),       # URL: /usuarios/crud/
    path('crear/', views.crear_usuario, name='crear_usuario'),      # URL: /usuarios/crear/
    path('registro/', views.registrar_usuario, name='registro'),    # URL: /usuarios/registro/
    path('login/', views.login_vista, name='login'),                # URL: /usuarios/login/
    path('logout/', views.logout_vista, name='logout'),             # URL: /usuarios/logout/
]
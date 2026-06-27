from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# 1. HOME: Accesible para todo el mundo
def home(request):
    return render(request, 'home.html')

# 2. REGISTRO PÚBLICO: Para que cualquiera cree su cuenta
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) # Inicia sesión automáticamente tras registrarse
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

# 3. LOGIN: Procesar el inicio de sesión
def login_vista(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 4. LOGOUT: Cerrar sesión
def logout_vista(request):
    logout(request)
    return redirect('home')

# 5. LEER (CRUD): ¡SÓLO PARA USUARIOS LOGUEADOS!
@login_required(login_url='login')
def leer_usuarios(request):
    todos_los_usuarios = User.objects.all()
    return render(request, 'leer.html', {'usuarios': todos_los_usuarios})

# 6. CREAR (CRUD): ¡SÓLO PARA USUARIOS LOGUEADOS! (Administración manual)
@login_required(login_url='login')
def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leer_usuarios')
    else:
        form = UserCreationForm()
    return render(request, 'crear.html', {'form': form})
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Cambié 'email' por 'username'
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('home')  # Redirigir al home después de iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas. Intenta de nuevo.')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después de registrarse
        else:
            messages.error(request, 'Por favor, completa todos los campos correctamente.')

    else:
        form = CustomUserCreationForm()  # Forma vacía para el registro

    # Modificación aquí: Aseguramos que si hay errores en el formulario, los campos llenados se mantengan
    return render(request, 'register.html', {'form': form})  # Pasamos el formulario con los datos actuales

#

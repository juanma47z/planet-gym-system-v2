from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('home')
        else:
            messages.error(request, 'Acceso inválido. Por favor, inténtelo otra vez.')
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Cierre de sesión exitoso")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)#No guarda inmediatamente
            user.teacher = form.cleaned_data.get('teacher', False) #guarda el valor
            user.save()
            login(request, user)  # Iniciar sesión automáticamente después de registrarse
            messages.success(request, 'Registro exitoso. Bienvenido a Planet Gym!')
            return redirect('home')
        else:
            messages.error(request, 'Error en el formulario. Verifica los datos.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})



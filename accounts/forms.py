from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    username = forms.CharField(label='Nombre usuario', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    teacher = forms.BooleanField(label='Profesor' , required=False)

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'teacher']

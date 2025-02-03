from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    id_number = forms.CharField(max_length=20, required=True)  # Cédula
    phone = forms.CharField(max_length=15, required=True)  # Teléfono
    username = forms.CharField(max_length=150, required=True)  # Cambié email por username

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'id_number', 'phone', 'password1', 'password2')  # Elimina 'email'



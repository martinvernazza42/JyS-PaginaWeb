from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Alumno
from .validators import validar_solo_letras, validar_email_gmail, validar_telefono_15_digitos

class AlumnoUserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        validators=[validar_solo_letras],
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        max_length=30,
        validators=[validar_solo_letras],
        widget=forms.TextInput(attrs={'placeholder': 'Apellido'})
    )
    email = forms.EmailField(
        validators=[validar_email_gmail],
        widget=forms.EmailInput(attrs={'placeholder': 'correo@gmail.com'})
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class AlumnoForm(forms.ModelForm):
    telefono = forms.CharField(
        max_length=15,
        validators=[validar_telefono_15_digitos],
        widget=forms.TextInput(attrs={'placeholder': '1234567890'}),
        required=False
    )
    
    class Meta:
        model = Alumno
        fields = ('dni', 'telefono', 'curso')
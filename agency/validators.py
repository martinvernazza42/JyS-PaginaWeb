from django.core.exceptions import ValidationError
import re

def validar_solo_letras(value):
    """
    Valida que el campo solo contenga letras, espacios y caracteres acentuados.
    No permite números ni caracteres especiales.
    """
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
        raise ValidationError('Este campo solo puede contener letras y espacios.')

def validar_telefono_15_digitos(value):
    """
    Valida que el teléfono contenga entre 10 y 15 dígitos numéricos.
    """
    if not re.match(r'^\d{10,15}$', value):
        raise ValidationError('El teléfono debe contener entre 10 y 15 números.')

def validar_email_gmail(value):
    """
    Valida que el email termine en @gmail.com
    """
    if not value.endswith('@gmail.com'):
        raise ValidationError('El email debe terminar en @gmail.com')

def validar_sin_numeros(value):
    """
    Valida que el campo no contenga números.
    """
    if re.search(r'\d', value):
        raise ValidationError('Este campo no puede contener números.')
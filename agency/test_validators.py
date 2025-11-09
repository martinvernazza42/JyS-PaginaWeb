from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Alumno
from .validators import validar_solo_letras, validar_telefono_15_digitos, validar_email_gmail

class ValidatorsTestCase(TestCase):
    
    def test_validar_solo_letras_valido(self):
        """Prueba que nombres válidos pasen la validación"""
        nombres_validos = [
            "Juan",
            "María José",
            "José Luis",
            "Ana María",
            "Ñoño",
            "José Ángel"
        ]
        for nombre in nombres_validos:
            try:
                validar_solo_letras(nombre)
            except ValidationError:
                self.fail(f"El nombre '{nombre}' debería ser válido")
    
    def test_validar_solo_letras_invalido(self):
        """Prueba que nombres con números fallen la validación"""
        nombres_invalidos = [
            "Juan123",
            "María2",
            "José-Luis",
            "Ana@María",
            "123",
            "Juan_Carlos"
        ]
        for nombre in nombres_invalidos:
            with self.assertRaises(ValidationError):
                validar_solo_letras(nombre)
    
    def test_validar_telefono_valido(self):
        """Prueba que teléfonos válidos pasen la validación"""
        telefonos_validos = [
            "123456789012345",
            "000000000000000",
            "999999999999999"
        ]
        for telefono in telefonos_validos:
            try:
                validar_telefono_15_digitos(telefono)
            except ValidationError:
                self.fail(f"El teléfono '{telefono}' debería ser válido")
    
    def test_validar_telefono_invalido(self):
        """Prueba que teléfonos inválidos fallen la validación"""
        telefonos_invalidos = [
            "12345678901234",  # 14 dígitos
            "1234567890123456",  # 16 dígitos
            "12345678901234a",  # contiene letra
            "123-456-789-012",  # contiene guiones
            "",  # vacío
            "abcdefghijklmno"  # solo letras
        ]
        for telefono in telefonos_invalidos:
            with self.assertRaises(ValidationError):
                validar_telefono_15_digitos(telefono)
    
    def test_validar_email_gmail_valido(self):
        """Prueba que emails de Gmail válidos pasen la validación"""
        emails_validos = [
            "usuario@gmail.com",
            "test.email@gmail.com",
            "123@gmail.com"
        ]
        for email in emails_validos:
            try:
                validar_email_gmail(email)
            except ValidationError:
                self.fail(f"El email '{email}' debería ser válido")
    
    def test_validar_email_gmail_invalido(self):
        """Prueba que emails que no sean de Gmail fallen la validación"""
        emails_invalidos = [
            "usuario@hotmail.com",
            "test@yahoo.com",
            "email@outlook.com",
            "usuario@gmail.es",
            "usuario@gmail"
        ]
        for email in emails_invalidos:
            with self.assertRaises(ValidationError):
                validar_email_gmail(email)

class AlumnoModelTestCase(TestCase):
    
    def setUp(self):
        """Configuración inicial para las pruebas"""
        self.user_data = {
            'username': 'testuser',
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'email': 'juan.perez@gmail.com'
        }
    
    def test_crear_alumno_valido(self):
        """Prueba crear un alumno con datos válidos"""
        user = User.objects.create(**self.user_data)
        alumno = Alumno.objects.create(
            user=user,
            dni='12345678',
            telefono='123456789012345'
        )
        self.assertEqual(alumno.user.first_name, 'Juan')
        self.assertEqual(alumno.telefono, '123456789012345')
    
    def test_alumno_nombre_con_numeros(self):
        """Prueba que un alumno con números en el nombre falle la validación"""
        user_data = self.user_data.copy()
        user_data['first_name'] = 'Juan123'
        user = User.objects.create(**user_data)
        
        alumno = Alumno(
            user=user,
            dni='12345678',
            telefono='123456789012345'
        )
        
        with self.assertRaises(ValidationError):
            alumno.full_clean()
    
    def test_alumno_telefono_invalido(self):
        """Prueba que un alumno con teléfono inválido falle la validación"""
        user = User.objects.create(**self.user_data)
        alumno = Alumno(
            user=user,
            dni='12345678',
            telefono='12345'  # Muy corto
        )
        
        with self.assertRaises(ValidationError):
            alumno.full_clean()
    
    def test_alumno_email_no_gmail(self):
        """Prueba que un alumno con email que no sea Gmail falle la validación"""
        user_data = self.user_data.copy()
        user_data['email'] = 'juan@hotmail.com'
        user = User.objects.create(**user_data)
        
        alumno = Alumno(
            user=user,
            dni='12345678',
            telefono='123456789012345'
        )
        
        with self.assertRaises(ValidationError):
            alumno.full_clean()
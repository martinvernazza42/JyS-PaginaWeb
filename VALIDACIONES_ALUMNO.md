# Validaciones para Alumnos - JyS Página Web

## Resumen de Validaciones Implementadas

Se han implementado las siguientes restricciones de datos para la creación de alumnos:

### 1. Nombre y Apellido
- **Restricción**: No se permiten números ni caracteres especiales
- **Permitido**: Solo letras (incluye acentos y ñ) y espacios
- **Ejemplos válidos**: 
  - "Juan"
  - "María José"
  - "José Ángel"
  - "Ñoño"
- **Ejemplos inválidos**:
  - "Juan123"
  - "María-José"
  - "Ana@María"

### 2. Teléfono
- **Restricción**: Solo números, exactamente 15 dígitos
- **Formato**: 15 dígitos consecutivos sin espacios ni guiones
- **Ejemplo válido**: "123456789012345"
- **Ejemplos inválidos**:
  - "12345678901234" (14 dígitos)
  - "1234567890123456" (16 dígitos)
  - "123-456-789-012" (con guiones)
  - "12345678901234a" (contiene letra)

### 3. Email
- **Restricción**: Debe terminar obligatoriamente en "@gmail.com"
- **Ejemplos válidos**:
  - "usuario@gmail.com"
  - "test.email@gmail.com"
  - "123@gmail.com"
- **Ejemplos inválidos**:
  - "usuario@hotmail.com"
  - "test@yahoo.com"
  - "usuario@gmail.es"

## Archivos Modificados/Creados

### 1. `agency/models.py`
- Agregados validadores al modelo `Alumno`
- Implementado método `clean()` para validación personalizada
- Sobrescrito método `save()` para ejecutar validaciones

### 2. `agency/validators.py` (NUEVO)
- Funciones de validación centralizadas:
  - `validar_solo_letras()`
  - `validar_telefono_15_digitos()`
  - `validar_email_gmail()`
  - `validar_sin_numeros()`

### 3. `agency/forms.py` (NUEVO)
- `AlumnoUserForm`: Formulario para crear usuarios con validaciones
- `AlumnoForm`: Formulario para datos específicos del alumno

### 4. `agency/admin.py`
- Configurado admin personalizado para usar los formularios con validaciones
- Integración con el sistema de usuarios de Django

### 5. `agency/test_validators.py` (NUEVO)
- Suite completa de pruebas para todas las validaciones
- 10 casos de prueba que verifican tanto casos válidos como inválidos

## Cómo Usar

### En el Admin de Django
1. Accede al admin de Django
2. Ve a la sección "Users" para crear un nuevo alumno
3. Las validaciones se aplicarán automáticamente al guardar

### En Formularios Personalizados
```python
from agency.forms import AlumnoUserForm, AlumnoForm

# Usar en vistas
form = AlumnoUserForm(request.POST)
if form.is_valid():
    user = form.save()
```

### Validación Programática
```python
from agency.validators import validar_solo_letras, validar_telefono_15_digitos

# Validar nombre
try:
    validar_solo_letras("Juan")  # OK
    validar_solo_letras("Juan123")  # Lanza ValidationError
except ValidationError as e:
    print(e.message)
```

## Ejecutar Pruebas

Para verificar que todas las validaciones funcionan correctamente:

```bash
# Activar entorno virtual
entornoFede\Scripts\activate

# Ejecutar pruebas
python manage.py test agency.test_validators
```

## Migraciones

Se creó la migración `0004_alter_alumno_telefono.py` que actualiza el campo teléfono con las nuevas validaciones.

Para aplicar:
```bash
python manage.py migrate
```

## Notas Técnicas

- Las validaciones se ejecutan tanto en el frontend (formularios) como en el backend (modelo)
- Se utiliza regex para validar patrones específicos
- Las validaciones son compatibles con caracteres especiales del español (acentos, ñ)
- El sistema es extensible para agregar más validaciones en el futuro
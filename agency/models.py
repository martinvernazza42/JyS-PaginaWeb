from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.dni}"

class Material(models.Model):
    TIPO_CHOICES = [
        ('apunte', 'Apunte'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('documento', 'Documento'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    archivo = models.FileField(upload_to='materiales/')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    cursos = models.ManyToManyField(Curso, blank=True)
    
    def __str__(self):
        return self.titulo



class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)
    fecha = models.DateField()
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.alumno} - {self.materia}: {self.calificacion}"

class MensajeProgramado(models.Model):
    TIPO_CHOICES = [
        ('recordatorio_examen', 'Recordatorio de Examen'),
        ('recordatorio_clase', 'Recordatorio de Clase'),
        ('recordatorio_tarea', 'Recordatorio de Tarea'),
        ('aviso_general', 'Aviso General'),
    ]
    
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_programada = models.DateTimeField()
    enviado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha_programada}"
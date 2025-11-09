from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Curso, Alumno, Material, Aviso, Nota, MensajeProgramado
from .forms import AlumnoUserForm, AlumnoForm

class AlumnoInline(admin.StackedInline):
    model = Alumno
    form = AlumnoForm
    can_delete = False
    verbose_name_plural = 'Información de Alumno'

class AlumnoUserAdmin(BaseUserAdmin):
    form = AlumnoUserForm
    inlines = (AlumnoInline,)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Solo para nuevos usuarios
            Alumno.objects.get_or_create(user=obj)

# Desregistrar el User admin por defecto y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, AlumnoUserAdmin)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    form = AlumnoForm
    list_display = ('get_nombre_completo', 'dni', 'telefono', 'curso', 'fecha_registro')
    list_filter = ('curso', 'fecha_registro')
    search_fields = ('user__first_name', 'user__last_name', 'dni')
    
    def get_nombre_completo(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_nombre_completo.short_description = 'Nombre Completo'

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'curso', 'fecha_subida')
    list_filter = ('tipo', 'curso', 'fecha_subida')
    search_fields = ('titulo', 'descripcion')

@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    list_filter = ('fecha_publicacion', 'cursos')
    search_fields = ('titulo', 'contenido')
    filter_horizontal = ('cursos',)

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'materia', 'calificacion', 'fecha')
    list_filter = ('materia', 'fecha')
    search_fields = ('alumno__user__first_name', 'alumno__user__last_name', 'materia')

@admin.register(MensajeProgramado)
class MensajeProgramadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'curso', 'fecha_programada', 'enviado')
    list_filter = ('tipo', 'curso', 'enviado', 'fecha_programada')
    search_fields = ('titulo', 'contenido')

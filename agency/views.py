from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from .models import Alumno, Curso, Material, Aviso, Nota, MensajeProgramado

def index(request):
    if request.method == 'POST':
        # Procesar formulario de contacto
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        message = request.POST.get('message')
        
        # Crear el contenido del correo
        subject = f'Nueva consulta de {name}'
        email_message = f"""
Nueva consulta recibida:

Nombre: {name}
Email: {email}
Teléfono: {phone}
Curso de interés: {course if course else 'No especificado'}

Mensaje:
{message}
"""
        
        # Enviar email en background para evitar timeout
        try:
            from threading import Thread
            
            def send_email_async():
                try:
                    send_mail(
                        subject,
                        email_message,
                        settings.DEFAULT_FROM_EMAIL,
                        ['martinver163@gmail.com'],
                        fail_silently=True,
                    )
                except:
                    pass  # Fallar silenciosamente
            
            # Ejecutar en hilo separado
            Thread(target=send_email_async, daemon=True).start()
            
        except:
            pass  # Si falla el threading, continuar
        
        # Siempre mostrar éxito para mejor UX
        messages.success(request, '¡Mensaje recibido! Te responderemos a la brevedad.')
        return redirect('index')
    
    return render(request, 'agency/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('seleccionar_curso')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, 'DNI o contraseña incorrectos')
    
    return render(request, 'agency/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def seleccionar_curso(request):
    if request.method == 'POST':
        curso_id = request.POST.get('curso_id')
        if curso_id:
            request.session['curso_seleccionado'] = int(curso_id)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Debes seleccionar un curso')
    
    cursos = Curso.objects.all()
    return render(request, 'agency/seleccionar_curso.html', {'cursos': cursos})

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    curso_id = request.session.get('curso_seleccionado')
    if not curso_id:
        return redirect('seleccionar_curso')
    
    curso_actual = get_object_or_404(Curso, id=curso_id)
    alumnos = Alumno.objects.filter(curso=curso_actual)
    materiales = Material.objects.filter(curso=curso_actual)[:5]
    avisos = Aviso.objects.filter(cursos=curso_actual)[:5]
    mensajes_programados = MensajeProgramado.objects.filter(curso=curso_actual, enviado=False)[:5]
    
    context = {
        'curso_actual': curso_actual,
        'alumnos_count': alumnos.count(),
        'materiales_count': Material.objects.filter(curso=curso_actual).count(),
        'avisos_count': Aviso.objects.filter(cursos=curso_actual).count(),
        'mensajes_programados_count': MensajeProgramado.objects.filter(curso=curso_actual, enviado=False).count(),
        'alumnos': alumnos,
        'materiales': materiales,
        'avisos': avisos,
        'mensajes_programados': mensajes_programados,
    }
    return render(request, 'agency/admin_dashboard.html', context)

@login_required
def student_dashboard(request):
    try:
        alumno = request.user.alumno
        materiales = Material.objects.filter(curso=alumno.curso) if alumno.curso else []
        avisos = Aviso.objects.filter(cursos=alumno.curso) if alumno.curso else []
        notas = Nota.objects.filter(alumno=alumno)
        asistencias = []
        
        context = {
            'alumno': alumno,
            'materiales': materiales,
            'avisos': avisos,
            'notas': notas,
            'asistencias': asistencias,
        }
        return render(request, 'agency/student_dashboard.html', context)
    except Alumno.DoesNotExist:
        messages.error(request, 'No tienes perfil de alumno asignado')
        return redirect('index')

@login_required
@user_passes_test(is_admin)
def crear_alumno(request):
    curso_id = request.session.get('curso_seleccionado')
    if not curso_id:
        return redirect('seleccionar_curso')
    
    curso_actual = get_object_or_404(Curso, id=curso_id)
    
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        
        # Verificar si ya existe un usuario con ese DNI
        if User.objects.filter(username=dni).exists():
            messages.error(request, f'Ya existe un alumno con el DNI {dni}')
        else:
            try:
                # Crear usuario
                user = User.objects.create_user(
                    username=dni,
                    password=dni,
                    first_name=nombre,
                    last_name=apellido,
                    email=email
                )
                
                # Crear alumno asignado al curso actual
                alumno = Alumno.objects.create(
                    user=user,
                    dni=dni,
                    telefono=telefono,
                    curso=curso_actual
                )
                
                messages.success(request, f'Alumno {nombre} {apellido} creado exitosamente en {curso_actual.nombre}')
                return redirect('admin_dashboard')
            except Exception as e:
                messages.error(request, f'Error al crear alumno: {str(e)}')
    
    return render(request, 'agency/crear_alumno.html', {'curso_actual': curso_actual})

@login_required
@user_passes_test(is_admin)
def subir_material(request):
    curso_id = request.session.get('curso_seleccionado')
    if not curso_id:
        return redirect('seleccionar_curso')
    
    curso_actual = get_object_or_404(Curso, id=curso_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        tipo = request.POST.get('tipo')
        archivo = request.FILES.get('archivo')
        
        Material.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            tipo=tipo,
            archivo=archivo,
            curso=curso_actual
        )
        
        messages.success(request, f'Material subido exitosamente a {curso_actual.nombre}')
        return redirect('admin_dashboard')
    
    return render(request, 'agency/subir_material.html', {'curso_actual': curso_actual})

@login_required
@user_passes_test(is_admin)
def gestionar_alumno(request, alumno_id):
    curso_id = request.session.get('curso_seleccionado')
    if not curso_id:
        return redirect('seleccionar_curso')
    
    curso_actual = get_object_or_404(Curso, id=curso_id)
    alumno = get_object_or_404(Alumno, id=alumno_id)
    notas = Nota.objects.filter(alumno=alumno).order_by('-fecha')
    asistencias = []
    
    context = {
        'alumno': alumno,
        'notas': notas,
        'asistencias': asistencias,
        'curso_actual': curso_actual,
    }
    return render(request, 'agency/gestionar_alumno.html', context)

@login_required
@user_passes_test(is_admin)
def editar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    cursos = Curso.objects.all()
    
    if request.method == 'POST':
        # Actualizar datos del usuario
        alumno.user.first_name = request.POST.get('nombre')
        alumno.user.last_name = request.POST.get('apellido')
        alumno.user.email = request.POST.get('email')
        
        # Actualizar datos del alumno
        alumno.dni = request.POST.get('dni')
        alumno.telefono = request.POST.get('telefono')
        curso_id = request.POST.get('curso')
        if curso_id:
            alumno.curso = get_object_or_404(Curso, id=curso_id)
        else:
            alumno.curso = None
        
        try:
            alumno.user.save()
            alumno.save()
            messages.success(request, 'Datos del alumno actualizados exitosamente')
            return redirect('gestionar_alumno', alumno_id=alumno.id)
        except Exception as e:
            messages.error(request, f'Error al actualizar: {str(e)}')
    
    context = {
        'alumno': alumno,
        'cursos': cursos,
    }
    return render(request, 'agency/editar_alumno.html', context)

@login_required
@user_passes_test(is_admin)
def borrar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    
    if request.method == 'POST':
        nombre_completo = f"{alumno.user.first_name} {alumno.user.last_name}"
        alumno.user.delete()  # Esto también borra el alumno por CASCADE
        messages.success(request, f'Alumno {nombre_completo} eliminado exitosamente')
        return redirect('admin_dashboard')
    
    return render(request, 'agency/confirmar_borrar_alumno.html', {'alumno': alumno})

@login_required
@user_passes_test(is_admin)
def agregar_nota(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    
    if request.method == 'POST':
        materia = request.POST.get('materia')
        calificacion = request.POST.get('calificacion')
        fecha = request.POST.get('fecha')
        observaciones = request.POST.get('observaciones')
        
        Nota.objects.create(
            alumno=alumno,
            materia=materia,
            calificacion=calificacion,
            fecha=fecha,
            observaciones=observaciones
        )
        
        messages.success(request, 'Nota agregada exitosamente')
        return redirect('gestionar_alumno', alumno_id=alumno.id)
    
    return render(request, 'agency/agregar_nota.html', {'alumno': alumno})



@login_required
@user_passes_test(is_admin)
def buscar_alumnos(request):
    query = request.GET.get('q', '')
    
    if query:
        alumnos = Alumno.objects.filter(
            models.Q(dni__icontains=query) |
            models.Q(user__first_name__icontains=query) |
            models.Q(user__last_name__icontains=query)
        )
    else:
        alumnos = Alumno.objects.all()
    
    return render(request, 'agency/buscar_alumnos.html', {
        'alumnos': alumnos,
        'query': query,
    })



@login_required
@user_passes_test(is_admin)
def crear_aviso(request):
    curso_id = request.session.get('curso_seleccionado')
    if not curso_id:
        return redirect('seleccionar_curso')
    
    curso_actual = get_object_or_404(Curso, id=curso_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        
        aviso = Aviso.objects.create(
            titulo=titulo,
            contenido=contenido
        )
        aviso.cursos.add(curso_actual)
        
        messages.success(request, f'Aviso publicado exitosamente para {curso_actual.nombre}')
        return redirect('admin_dashboard')
    
    return render(request, 'agency/crear_aviso.html', {'curso_actual': curso_actual})

@login_required
@user_passes_test(is_admin)
def programar_mensaje(request):
    curso_id = request.session.get('curso_seleccionado')
    if not curso_id:
        return redirect('seleccionar_curso')
    
    curso_actual = get_object_or_404(Curso, id=curso_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        tipo = request.POST.get('tipo')
        fecha_programada = request.POST.get('fecha_programada')
        
        MensajeProgramado.objects.create(
            titulo=titulo,
            contenido=contenido,
            tipo=tipo,
            curso=curso_actual,
            fecha_programada=fecha_programada
        )
        
        messages.success(request, f'Mensaje programado exitosamente para {curso_actual.nombre}')
        return redirect('admin_dashboard')
    
    return render(request, 'agency/programar_mensaje.html', {'curso_actual': curso_actual})
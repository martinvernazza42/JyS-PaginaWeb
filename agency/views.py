from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

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
        
        try:
            # Enviar correo
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                ['martinver163@gmail.com'],
                fail_silently=False,
            )
            return HttpResponse("¡Mensaje enviado exitosamente! Te responderemos a la brevedad.")
        except Exception as e:
            return HttpResponse("Error al enviar el mensaje. Por favor, intenta nuevamente.")
    
    return render(request, 'agency/index.html')
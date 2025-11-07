from django.core.management.base import BaseCommand
from django.utils import timezone
from agency.models import MensajeProgramado, Aviso

class Command(BaseCommand):
    help = 'Procesa mensajes programados y los convierte en avisos'

    def handle(self, *args, **options):
        ahora = timezone.now()
        mensajes_pendientes = MensajeProgramado.objects.filter(
            fecha_programada__lte=ahora,
            enviado=False
        )
        
        mensajes_procesados = 0
        
        for mensaje in mensajes_pendientes:
            # Crear aviso a partir del mensaje programado
            aviso = Aviso.objects.create(
                titulo=mensaje.titulo,
                contenido=mensaje.contenido
            )
            aviso.cursos.add(mensaje.curso)
            
            # Marcar mensaje como enviado
            mensaje.enviado = True
            mensaje.save()
            
            mensajes_procesados += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Mensaje procesado: {mensaje.titulo}')
            )
        
        if mensajes_procesados == 0:
            self.stdout.write(
                self.style.WARNING('No hay mensajes programados para procesar')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Se procesaron {mensajes_procesados} mensajes programados')
            )
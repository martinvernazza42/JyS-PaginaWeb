from django.core.management.base import BaseCommand
from agency.models import Curso

class Command(BaseCommand):
    help = 'Crea los cursos predefinidos de la academia'

    def handle(self, *args, **options):
        cursos = [
            {
                'nombre': 'Cursos para Niños (Kids English)',
                'descripcion': 'Clases dinámicas con juegos, canciones y actividades que estimulan el aprendizaje natural del idioma para niños desde los 5 años.'
            },
            {
                'nombre': 'Cursos para Adolescentes (Teens English)',
                'descripcion': 'Clases enfocadas en comunicación real, adaptadas a los intereses de los adolescentes de 12 a 17 años.'
            },
            {
                'nombre': 'Cursos para Adultos (Adults English)',
                'descripcion': 'Ideal para quienes desean retomar el inglés, viajar, o mejorar su desempeño profesional.'
            },
            {
                'nombre': 'Inglés para Empresas (Business English)',
                'descripcion': 'Entrenamiento lingüístico personalizado para equipos de trabajo y comunicación profesional.'
            },
            {
                'nombre': 'Cursos Intensivos',
                'descripcion': 'Programas acelerados para quienes necesitan resultados rápidos en 1 a 3 meses.'
            },
            {
                'nombre': 'Preparación para Exámenes Internacionales',
                'descripcion': 'Clases enfocadas en estrategias de examen para Cambridge, TOEFL, IELTS, Trinity.'
            }
        ]

        for curso_data in cursos:
            curso, created = Curso.objects.get_or_create(
                nombre=curso_data['nombre'],
                defaults={'descripcion': curso_data['descripcion']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Curso creado: {curso.nombre}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Curso ya existe: {curso.nombre}')
                )

        self.stdout.write(
            self.style.SUCCESS('Proceso completado. Todos los cursos están disponibles.')
        )
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('seleccionar-curso/', views.seleccionar_curso, name='seleccionar_curso'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('crear-alumno/', views.crear_alumno, name='crear_alumno'),
    path('subir-material/', views.subir_material, name='subir_material'),
    path('gestionar-alumno/<int:alumno_id>/', views.gestionar_alumno, name='gestionar_alumno'),
    path('agregar-nota/<int:alumno_id>/', views.agregar_nota, name='agregar_nota'),

    path('buscar-alumnos/', views.buscar_alumnos, name='buscar_alumnos'),

    path('crear-aviso/', views.crear_aviso, name='crear_aviso'),
    path('programar-mensaje/', views.programar_mensaje, name='programar_mensaje'),
]
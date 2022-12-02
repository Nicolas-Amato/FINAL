from django.urls import path
from . import views
from .forms import club_deportivoForm, profesorForm, alumnoForm


urlpatterns = [
    path('', views.index),
    path('nuevo_deporte/', views.nuevo_deporte, name='Nuevo Deporte'),
    path('nuevo_profesor/', views.nuevo_profesor, name='Nuevo Profesor'),
    path('nuevo_alumno/', views.nuevo_alumno, name='Nuevo Alumno'),
    path('buscar_DEPORTE/',views.buscar_DEPORTE, name='buscar DEPORTE'),
    path('buscar_profesor/', views.buscar_profesor, name='buscar PROFESOR'),
    path('mostrar_profesores/', views.mostrar_profesores, name='mostrar PROFESORES'),
    path('eliminar_profesor/<DNI_profesor>', views.eliminar_profesor, name='eliminar PROFESORES'),
    path('modif_profesor/<DNI_profesor>', views.modif_profesor, name='modificar PROFESORES'),
    path('club_deportivoForm/', club_deportivoForm),
    path('profesorForm/', profesorForm),
    path('alumnoForm/', alumnoForm),
    path('deporte_list/', views.club_deportivoList.as_view(), name='List'),
    path('deporte_detalle/<pk>', views.club_deportivoDetailView.as_view(), name='Detail'),
    path('deporte_confirm_delete/<pk>', views.club_deportivoDeleteView.as_view(), name='Delete')
]





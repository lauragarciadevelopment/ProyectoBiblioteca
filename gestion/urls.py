from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/<int:pk>/', views.detalle_autor, name='detalle_autor'),

    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),

    path('socios/', views.lista_socios, name='lista_socios'),
    path('socios/<int:pk>/', views.detalle_socio, name='detalle_socio'),

    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/<int:pk>/', views.detalle_prestamo, name='detalle_prestamo'),
]

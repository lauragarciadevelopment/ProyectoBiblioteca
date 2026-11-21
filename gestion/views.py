from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from .models import Autor, Libro, Socio, Prestamo


# ------------------------------------------------------------------
# Página de inicio: resumen y acceso a todas las tablas
# ------------------------------------------------------------------
def inicio(request):
    contexto = {
        'total_autores': Autor.objects.count(),
        'total_libros': Libro.objects.count(),
        'total_socios': Socio.objects.count(),
        'total_prestamos': Prestamo.objects.count(),
        'prestamos_activos': Prestamo.objects.filter(devuelto=False).count(),
    }
    return render(request, 'gestion/inicio.html', contexto)


# ------------------------------------------------------------------
# READ - AUTORES
# ------------------------------------------------------------------
def lista_autores(request):
    # annotate agrega a cada autor el número de libros relacionados
    autores = Autor.objects.annotate(num_libros=Count('libros')).order_by('nombre')
    return render(request, 'gestion/autor_list.html', {'autores': autores})


def detalle_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    # related_name='libros' permite consultar los libros de este autor
    libros = autor.libros.all().order_by('titulo')
    return render(request, 'gestion/autor_detail.html', {'autor': autor, 'libros': libros})


# ------------------------------------------------------------------
# READ - LIBROS (llave foránea a Autor)
# ------------------------------------------------------------------
def lista_libros(request):
    # select_related trae el autor en la misma consulta (JOIN)
    libros = Libro.objects.select_related('autor').order_by('titulo')
    return render(request, 'gestion/libro_list.html', {'libros': libros})


def detalle_libro(request, pk):
    libro = get_object_or_404(Libro.objects.select_related('autor'), pk=pk)
    prestamos = libro.prestamos.select_related('socio').order_by('-fecha_prestamo')
    return render(request, 'gestion/libro_detail.html', {'libro': libro, 'prestamos': prestamos})


# ------------------------------------------------------------------
# READ - SOCIOS
# ------------------------------------------------------------------
def lista_socios(request):
    socios = Socio.objects.annotate(
        prestamos_activos=Count('prestamos', filter=Q(prestamos__devuelto=False))
    ).order_by('nombre')
    return render(request, 'gestion/socio_list.html', {'socios': socios})


def detalle_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    prestamos = socio.prestamos.select_related('libro', 'libro__autor').order_by('-fecha_prestamo')
    return render(request, 'gestion/socio_detail.html', {'socio': socio, 'prestamos': prestamos})


# ------------------------------------------------------------------
# READ - PRÉSTAMOS (llaves foráneas a Libro y Socio)
# ------------------------------------------------------------------
def lista_prestamos(request):
    prestamos = Prestamo.objects.select_related('libro', 'libro__autor', 'socio') \
        .order_by('devuelto', '-fecha_prestamo')
    return render(request, 'gestion/prestamo_list.html', {'prestamos': prestamos})


def detalle_prestamo(request, pk):
    prestamo = get_object_or_404(
        Prestamo.objects.select_related('libro', 'libro__autor', 'socio'), pk=pk
    )
    return render(request, 'gestion/prestamo_detail.html', {'prestamo': prestamo})

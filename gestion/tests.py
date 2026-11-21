from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Autor, Libro, Socio, Prestamo


class ReadTests(TestCase):
    """Pruebas de la operación READ (listado y detalle) de todas las tablas."""

    @classmethod
    def setUpTestData(cls):
        cls.autor = Autor.objects.create(nombre='Autor Prueba', nacionalidad='Colombiana')
        cls.libro = Libro.objects.create(titulo='Libro Prueba', isbn='1234567890123',
                                         anio_publicacion=2020, copias_disponibles=2,
                                         autor=cls.autor)
        cls.socio = Socio.objects.create(nombre='Socio Prueba', documento='111',
                                         email='socio@test.co')
        cls.prestamo = Prestamo.objects.create(libro=cls.libro, socio=cls.socio)

    def test_inicio(self):
        self.assertEqual(self.client.get(reverse('inicio')).status_code, 200)

    def test_listados(self):
        self.assertContains(self.client.get(reverse('lista_autores')), 'Autor Prueba')
        # Las llaves foráneas se muestran con el nombre del objeto relacionado
        r = self.client.get(reverse('lista_libros'))
        self.assertContains(r, 'Libro Prueba')
        self.assertContains(r, 'Autor Prueba')
        self.assertContains(self.client.get(reverse('lista_socios')), 'Socio Prueba')
        r = self.client.get(reverse('lista_prestamos'))
        self.assertContains(r, 'Libro Prueba')
        self.assertContains(r, 'Socio Prueba')

    def test_detalles(self):
        self.assertContains(self.client.get(reverse('detalle_autor', args=[self.autor.pk])), 'Libro Prueba')
        self.assertContains(self.client.get(reverse('detalle_libro', args=[self.libro.pk])), 'Socio Prueba')
        self.assertContains(self.client.get(reverse('detalle_socio', args=[self.socio.pk])), 'Libro Prueba')
        r = self.client.get(reverse('detalle_prestamo', args=[self.prestamo.pk]))
        self.assertContains(r, 'Autor Prueba')
        self.assertContains(r, 'Prestado')

    def test_detalle_inexistente_da_404(self):
        for nombre in ['detalle_autor', 'detalle_libro', 'detalle_socio', 'detalle_prestamo']:
            self.assertEqual(self.client.get(reverse(nombre, args=[999])).status_code, 404)

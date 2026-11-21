from django.contrib import admin

from .models import Autor, Libro, Socio, Prestamo

# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Socio)
admin.site.register(Prestamo)

# Biblioteca - Gestión de préstamos

**Aplicación:** Biblioteca Django (app `gestion`)
**Temática:** Gestión de bibliotecas
**Propósito:** Administrar autores, libros, socios y préstamos, controlando la disponibilidad de ejemplares y las devoluciones.

## Modelos
- **Autor**: nombre, nacionalidad.
- **Libro**: título, ISBN, año de publicación, copias disponibles. Relacionado con Autor.
- **Socio**: nombre, documento, email, teléfono, fecha de registro.
- **Prestamo**: fecha de préstamo, fecha de devolución, devuelto. Relacionado con Libro y Socio.

## Cómo ejecutarlo
1. python -m venv venv
2. venv\Scripts\activate
3. pip install django
4. python manage.py migrate
5. python manage.py runserver
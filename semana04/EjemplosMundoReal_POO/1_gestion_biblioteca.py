"""
1_gestion_biblioteca.py
Modela una biblioteca con clases: Libro, Usuario, Prestamo.
Demuestra relaciones 1:N y control de estados (disponible/prestado).
"""

class Libro:
    """Representa un libro físico con ISBN único."""
    def __init__(self, isbn, titulo, autor, anio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True
        self.prestamos = []

    def prestar_a(self, usuario, dias=14):
        if self.disponible:
            prestamo = Prestamo(self, usuario, dias)
            self.prestamos.append(prestamo)
            self.disponible = False
            return prestamo
        else:
            raise ValueError(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        if self.prestamos and not self.disponible:
            self.prestamos[-1].finalizar()
            self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} ({self.anio}) — {estado}"


class Usuario:
    """Representa a una persona registrada en la biblioteca."""
    def __init__(self, id_usuario, nombre, tipo="Estudiante"):
        self.id = id_usuario
        self.nombre = nombre
        self.tipo = tipo  # "Estudiante", "Docente", "Personal"
        self.prestamos_activos = []

    def tomar_prestado(self, libro):
        prestamo = libro.prestar_a(self)
        self.prestamos_activos.append(prestamo)
        return prestamo

    def devolver_libro(self, libro):
        libro.devolver()
        self.prestamos_activos = [p for p in self.prestamos_activos if p.libro != libro]


class Prestamo:
    """Representa un evento de préstamo con fechas de inicio y devolución."""
    def __init__(self, libro, usuario, dias):
        from datetime import datetime, timedelta
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias)
        self.fecha_real_devolucion = None

    def finalizar(self):
        from datetime import datetime
        self.fecha_real_devolucion = datetime.now()

    def esta_vencido(self):
        from datetime import datetime
        return not self.fecha_real_devolucion and datetime.now() > self.fecha_devolucion

    def __str__(self):
        estado = "Vencido" if self.esta_vencido() else "Activo"
        return f"Prest. '{self.libro.titulo}' → {self.usuario.nombre} | {estado}"


# === Ejemplo de uso ===
if __name__ == "__main__":
    libro1 = Libro("978-3-16-148410-0", "Introducción a Python", "Ana Gómez", 2023)
    estudiante = Usuario("U-205", "David Mora")

    prestamo = estudiante.tomar_prestado(libro1)
    print(libro1)
    print(prestamo)
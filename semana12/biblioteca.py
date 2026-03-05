class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # 1. TUPLA: Almacena atributos inmutables (título y autor)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info[0]}' por {self.info[1]} (Cat: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, ci_usuario):
        self.nombre = nombre
        self.ci_usuario = ci_usuario
        # 2. LISTA: Gestiona los libros prestados al usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (C.I.: {self.ci_usuario})"


class Biblioteca:
    def __init__(self):
        # 3. DICCIONARIO: Almacena libros usando el ISBN como clave
        self.libros_disponibles = {}
        # 4. CONJUNTO (Set): Asegura números de C.I. únicos
        self.ci_usuarios = set()
        # Diccionario auxiliar para acceder rápido a los objetos Usuario mediante su C.I.
        self.usuarios = {}

    def añadir_libro(self, libro, mostrar_mensaje=True):
        self.libros_disponibles[libro.isbn] = libro
        if mostrar_mensaje:
            print(f"\n✅ Libro '{libro.info[0]}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"\n🗑️ Libro '{eliminado.info[0]}' eliminado del sistema.")
        else:
            print("\n⚠️ Error: No se encontró ningún libro con ese ISBN.")

    def buscar_libro(self, busqueda, por="titulo"):
        resultados = []
        for libro in self.libros_disponibles.values():
            if por == "1" and busqueda.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif por == "2" and busqueda.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif por == "3" and busqueda.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def registrar_usuario(self, usuario, mostrar_mensaje=True):
        if usuario.ci_usuario in self.ci_usuarios:
            if mostrar_mensaje:
                print(f"\n⚠️ Error: La C.I. {usuario.ci_usuario} ya está registrada en el sistema.")
        else:
            self.ci_usuarios.add(usuario.ci_usuario)
            self.usuarios[usuario.ci_usuario] = usuario
            if mostrar_mensaje:
                print(f"\n👤 Usuario '{usuario.nombre}' registrado con éxito.")

    def dar_baja_usuario(self, ci_usuario):
        if ci_usuario in self.ci_usuarios:
            usuario = self.usuarios[ci_usuario]
            if len(usuario.libros_prestados) == 0:
                self.ci_usuarios.remove(ci_usuario)
                del self.usuarios[ci_usuario]
                print(f"\n👋 Usuario '{usuario.nombre}' dado de baja.")
            else:
                print(f"\n⚠️ El usuario {usuario.nombre} tiene libros pendientes. No se puede dar de baja.")
        else:
            print("\n⚠️ Error: Usuario no encontrado con esa C.I.")

    def prestar_libro(self, ci_usuario, isbn):
        if ci_usuario not in self.ci_usuarios:
            print("\n⚠️ Error: Usuario no registrado (C.I. incorrecta).")
            return
        if isbn not in self.libros_disponibles:
            print("\n⚠️ Error: El libro no está disponible o el ISBN es incorrecto.")
            return

        usuario = self.usuarios[ci_usuario]
        libro = self.libros_disponibles.pop(isbn)  # Sale del diccionario
        usuario.libros_prestados.append(libro)  # Entra a la lista del usuario
        print(f"\n✅ Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, ci_usuario, isbn):
        if ci_usuario not in self.ci_usuarios:
            print("\n⚠️ Error: Usuario no encontrado con esa C.I.")
            return

        usuario = self.usuarios[ci_usuario]
        for i, libro in enumerate(usuario.libros_prestados):
            if libro.isbn == isbn:
                libro_devuelto = usuario.libros_prestados.pop(i)  # Sale de la lista
                self.libros_disponibles[isbn] = libro_devuelto  # Vuelve al diccionario
                print(f"\n✅ Libro '{libro_devuelto.info[0]}' devuelto a la biblioteca.")
                return
        print(f"\n⚠️ El usuario no tiene un libro con ISBN {isbn} prestado.")

    def listar_libros_prestados(self, ci_usuario):
        if ci_usuario in self.ci_usuarios:
            usuario = self.usuarios[ci_usuario]
            print(f"\n📚 Libros actualmente prestados a {usuario.nombre} (C.I. {usuario.ci_usuario}):")
            if not usuario.libros_prestados:
                print(" - Ninguno.")
            else:
                for libro in usuario.libros_prestados:
                    print(f" - {libro}")
        else:
            print("\n⚠️ Error: Usuario no encontrado.")


# ==========================================
# MENÚ INTERACTIVO Y DATOS DE EJEMPLO
# ==========================================
def iniciar_sistema():
    sistema = Biblioteca()

    # --- CARGA DE DATOS DE EJEMPLO ---
    print("Cargando base de datos inicial...")

    # Libros de ejemplo
    sistema.añadir_libro(Libro("Aprende Python 3", "Guido van Rossum", "Programacion", "PY-001"), False)
    sistema.añadir_libro(Libro("Diseño de Interfaces Modernas", "Alan Cooper", "Diseño", "UI-002"), False)
    sistema.añadir_libro(Libro("Cultura Montubia Ecuatoriana", "Willigton Paredes", "Historia", "EC-003"), False)
    sistema.añadir_libro(Libro("El señor de los anillos", "J.R.R. Tolkien", "Ficcion", "FIC-004"), False)

    # Usuarios de ejemplo (Ahora con Cédula de Identidad)
    sistema.registrar_usuario(Usuario("Ana López", "123456789"), False)
    sistema.registrar_usuario(Usuario("Carlos Vera", "987654321"), False)
    sistema.registrar_usuario(Usuario("María Sánchez", "112233445"), False)

    print("¡Datos cargados con éxito!\n")
    # ---------------------------------

    while True:
        print("\n" + "=" * 40)
        print("  SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("=" * 40)
        print("1. Añadir un libro")
        print("2. Quitar un libro")
        print("3. Registrar un usuario")
        print("4. Dar de baja un usuario")
        print("5. Prestar un libro")
        print("6. Devolver un libro")
        print("7. Buscar un libro")
        print("8. Ver libros prestados de un usuario")
        print("9. Salir del sistema")
        print("=" * 40)

        opcion = input("Elige una opción (1-9): ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN (ej. 1234): ")
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            sistema.añadir_libro(nuevo_libro)

        elif opcion == "2":
            isbn = input("Ingresa el ISBN del libro a eliminar: ")
            sistema.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            ci_usuario = input("C.I. del usuario (ej. 123456789): ")
            nuevo_usuario = Usuario(nombre, ci_usuario)
            sistema.registrar_usuario(nuevo_usuario)

        elif opcion == "4":
            ci_usuario = input("Ingresa la C.I. del usuario a dar de baja (ej. 123456789): ")
            sistema.dar_baja_usuario(ci_usuario)

        elif opcion == "5":
            print("\nC.I. de ejemplo: 123456789, 987654321, 112233445")
            ci_usuario = input("Ingresa la C.I. del usuario (ej. 123456789): ")
            print("ISBNs de ejemplo: PY-001, UI-002, EC-003, FIC-004")
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            sistema.prestar_libro(ci_usuario, isbn)

        elif opcion == "6":
            ci_usuario = input("Ingresa la C.I. del usuario (ej. 123456789): ")
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            sistema.devolver_libro(ci_usuario, isbn)

        elif opcion == "7":
            print("\n¿Por qué criterio deseas buscar?")
            print("1. Título\n2. Autor\n3. Categoría")
            criterio = input("Elige una opción (1-3): ")
            if criterio in ["1", "2", "3"]:
                busqueda = input("Ingresa tu búsqueda (ej. Programacion, Diseño, Ficcion): ")
                resultados = sistema.buscar_libro(busqueda, por=criterio)
                if resultados:
                    print("\n🔎 Resultados encontrados:")
                    for r in resultados:
                        print(f" - {r}")
                else:
                    print("\n❌ No se encontraron libros con esa búsqueda.")
            else:
                print("\n⚠️ Opción de búsqueda no válida.")

        elif opcion == "8":
            ci_usuario = input("Ingresa la C.I. del usuario (ej. 123456789): ")
            sistema.listar_libros_prestados(ci_usuario)

        elif opcion == "9":
            print("\nSaliendo del sistema de biblioteca. ¡Hasta luego! 👋")
            break

        else:
            print("\n⚠️ Opción no válida. Por favor, elige un número del 1 al 9.")


# Iniciar el programa
if __name__ == "__main__":
    iniciar_sistema()
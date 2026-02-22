#!/usr/bin/env python3
"""
Sistema de Gestion de Inventarios - Interfaz de Consola
Menú interactivo con manejo de errores, validación y persistencia.
"""

from inventario import Inventario
from producto import Producto
import sys

def leer_entero(mensaje: str, positivo: bool = True) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if positivo and valor <= 0:
                print("Error: El valor debe ser un número positivo")
                continue
            return valor
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero")

def leer_float(mensaje: str, positivo: bool = True) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if positivo and valor < 0:
                print("Error: El valor no puede ser negativo")
                continue
            return valor
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número válido")

def leer_texto(mensaje: str, min_longitud: int = 1) -> str:
    while True:
        texto = input(mensaje).strip()
        if len(texto) < min_longitud:
            print(f"Error: El texto debe tener al menos {min_longitud} carácter(es)")
            continue
        return texto

def mostrar_lista_productos(productos: list):
    if not productos:
        print("\nAdvertencia: No se encontraron productos")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<6} | {'NOMBRE':<22} | {'CANTIDAD':<10} | {'PRECIO':<12}")
    print("=" * 70)
    for producto in productos:
        print(f"{producto.id:<6} | {producto.nombre:<22} | {producto.cantidad:<10} | ${producto.precio:<11.2f}")
    print("=" * 70)
    print(f"Total: {len(productos)} producto(s)")

def menu_agregar(inventario: Inventario):
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    id_prod = leer_entero("ID del producto: ")

    if inventario.buscar_por_id(id_prod):
        print(f"\nError: Ya existe un producto con ID {id_prod}")
        return

    nombre = leer_texto("Nombre del producto: ")
    cantidad = leer_entero("Cantidad inicial: ", positivo=False)
    precio = leer_float("Precio unitario: $")

    producto = Producto(id_prod, nombre, cantidad, precio)

    try:
        if inventario.agregar_producto(producto):
            print(f"\n[ÉXITO] Producto '{nombre}' agregado y guardado en archivo correctamente.")
        else:
            print("\n[ERROR] No se pudo agregar el producto.")
    except PermissionError as e:
        print(f"\n[ADVERTENCIA] Producto agregado en memoria, pero falló el guardado: {e}")
    except Exception as e:
        print(f"\n[ERROR CRÍTICO] Ocurrió un problema al guardar en el archivo: {e}")

def menu_eliminar(inventario: Inventario):
    if inventario.esta_vacio():
        print("\nAdvertencia: El inventario está vacío")
        return

    print("\n--- ELIMINAR PRODUCTO ---")
    id_prod = leer_entero("ID del producto a eliminar: ")

    try:
        if inventario.eliminar_producto(id_prod):
            print(f"\n[ÉXITO] Producto con ID {id_prod} eliminado y cambios guardados en archivo.")
        else:
            print(f"\n[ERROR] No se encontró producto con ID {id_prod}")
    except PermissionError as e:
        print(f"\n[ADVERTENCIA] Producto eliminado en memoria, pero falló el guardado: {e}")
    except Exception as e:
        print(f"\n[ERROR CRÍTICO] Ocurrió un problema al guardar en el archivo: {e}")

def menu_actualizar(inventario: Inventario):
    if inventario.esta_vacio():
        print("\nAdvertencia: El inventario está vacío")
        return

    print("\n--- ACTUALIZAR PRODUCTO ---")
    print("1. Actualizar cantidad")
    print("2. Actualizar precio")
    opcion = input("Seleccione opción (1-2): ").strip()

    id_prod = leer_entero("ID del producto: ")
    producto = inventario.buscar_por_id(id_prod)

    if not producto:
        print(f"\nError: No se encontró producto con ID {id_prod}")
        return

    try:
        if opcion == '1':
            nueva_cantidad = leer_entero("Nueva cantidad: ", positivo=False)
            if inventario.actualizar_cantidad(id_prod, nueva_cantidad):
                print(f"\n[ÉXITO] Cantidad actualizada y guardada: {producto.nombre} -> {nueva_cantidad} unidades")
        elif opcion == '2':
            nuevo_precio = leer_float("Nuevo precio: $")
            if inventario.actualizar_precio(id_prod, nuevo_precio):
                print(f"\n[ÉXITO] Precio actualizado y guardado: {producto.nombre} -> ${nuevo_precio:.2f}")
        else:
            print("\nError: Opción no válida")
    except PermissionError as e:
        print(f"\n[ADVERTENCIA] Actualizado en memoria, pero falló el guardado: {e}")
    except Exception as e:
        print(f"\n[ERROR CRÍTICO] Ocurrió un problema al guardar en el archivo: {e}")

def menu_buscar(inventario: Inventario):
    if inventario.esta_vacio():
        print("\nAdvertencia: El inventario está vacío")
        return

    print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
    nombre_busqueda = leer_texto("Ingrese nombre o parte del nombre: ")
    resultados = inventario.buscar_por_nombre(nombre_busqueda)
    mostrar_lista_productos(resultados)

def menu_mostrar_todos(inventario: Inventario):
    if inventario.esta_vacio():
        print("\nEl inventario está vacío")
        return

    print("\n--- INVENTARIO COMPLETO ---")
    productos = inventario.obtener_todos()
    mostrar_lista_productos(productos)

def mostrar_menu():
    print("\n" + "=" * 50)
    print("   SISTEMA DE GESTION DE INVENTARIOS")
    print("=" * 50)
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("=" * 50)

def main():
    # Al inicializar, Inventario intentará cargar "inventario.json"
    inventario = Inventario()

    # Si el inventario está vacío (primera vez que se ejecuta o archivo borrado),
    # agregamos los datos de prueba automáticamente.
    if inventario.esta_vacio():
        print("\n[INFO] El inventario está vacío. Añadiendo productos de ejemplo...")
        inventario.agregar_producto(Producto(1, "Laptop", 10, 850.00))
        inventario.agregar_producto(Producto(2, "Mouse", 50, 25.50))
        inventario.agregar_producto(Producto(3, "Teclado", 30, 45.00))
        print("[INFO] Productos de ejemplo guardados en el archivo.")

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ").strip()

        if opcion == '1':
            menu_agregar(inventario)
        elif opcion == '2':
            menu_eliminar(inventario)
        elif opcion == '3':
            menu_actualizar(inventario)
        elif opcion == '4':
            menu_buscar(inventario)
        elif opcion == '5':
            menu_mostrar_todos(inventario)
        elif opcion == '6':
            print("\nGuardando últimos detalles y saliendo. ¡Gracias por usar el sistema!\n")
            sys.exit(0)
        else:
            print("\nError: Opción no válida. Por favor seleccione 1-6")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Sistema de Gestion de Inventarios - Interfaz de Consola
Menu interactivo con manejo de errores y validacion de entradas.
"""

from inventario import Inventario
from producto import Producto
import sys


def leer_entero(mensaje: str, positivo: bool = True) -> int:
    """Solicita y valida entrada de numero entero"""
    while True:
        try:
            valor = int(input(mensaje))
            if positivo and valor <= 0:
                print("Error: El valor debe ser un numero positivo")
                continue
            return valor
        except ValueError:
            print("Error: Entrada invalida. Debe ingresar un numero entero")


def leer_float(mensaje: str, positivo: bool = True) -> float:
    """Solicita y valida entrada de numero decimal"""
    while True:
        try:
            valor = float(input(mensaje))
            if positivo and valor < 0:
                print("Error: El valor no puede ser negativo")
                continue
            return valor
        except ValueError:
            print("Error: Entrada invalida. Debe ingresar un numero valido")


def leer_texto(mensaje: str, min_longitud: int = 1) -> str:
    """Solicita y valida entrada de texto"""
    while True:
        texto = input(mensaje).strip()
        if len(texto) < min_longitud:
            print(f"Error: El texto debe tener al menos {min_longitud} caracter(es)")
            continue
        return texto


def mostrar_producto(producto: Producto):
    """Muestra un producto con formato mejorado"""
    print(f"  {producto}")


def mostrar_lista_productos(productos: list):
    """Muestra una lista de productos con encabezado"""
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
    """Opcion: Agregar nuevo producto"""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    id_prod = leer_entero("ID del producto: ")

    if inventario.buscar_por_id(id_prod):
        print(f"\nError: Ya existe un producto con ID {id_prod}")
        return

    nombre = leer_texto("Nombre del producto: ")
    cantidad = leer_entero("Cantidad inicial: ", positivo=False)
    precio = leer_float("Precio unitario: $")

    producto = Producto(id_prod, nombre, cantidad, precio)
    if inventario.agregar_producto(producto):
        print(f"\nProducto '{nombre}' agregado exitosamente")
    else:
        print("\nError: No se pudo agregar el producto")


def menu_eliminar(inventario: Inventario):
    """Opcion: Eliminar producto"""
    if inventario.esta_vacio():
        print("\nAdvertencia: El inventario esta vacio")
        return

    print("\n--- ELIMINAR PRODUCTO ---")
    id_prod = leer_entero("ID del producto a eliminar: ")

    if inventario.eliminar_producto(id_prod):
        print(f"\nProducto con ID {id_prod} eliminado exitosamente")
    else:
        print(f"\nError: No se encontro producto con ID {id_prod}")


def menu_actualizar(inventario: Inventario):
    """Opcion: Actualizar producto"""
    if inventario.esta_vacio():
        print("\nAdvertencia: El inventario esta vacio")
        return

    print("\n--- ACTUALIZAR PRODUCTO ---")
    print("1. Actualizar cantidad")
    print("2. Actualizar precio")
    opcion = input("Seleccione opcion (1-2): ").strip()

    id_prod = leer_entero("ID del producto: ")
    producto = inventario.buscar_por_id(id_prod)

    if not producto:
        print(f"\nError: No se encontro producto con ID {id_prod}")
        return

    if opcion == '1':
        nueva_cantidad = leer_entero("Nueva cantidad: ", positivo=False)
        if inventario.actualizar_cantidad(id_prod, nueva_cantidad):
            print(f"\nCantidad actualizada: {producto.nombre} -> {nueva_cantidad} unidades")
    elif opcion == '2':
        nuevo_precio = leer_float("Nuevo precio: $")
        if inventario.actualizar_precio(id_prod, nuevo_precio):
            print(f"\nPrecio actualizado: {producto.nombre} -> ${nuevo_precio:.2f}")
    else:
        print("\nError: Opcion no valida")


def menu_buscar(inventario: Inventario):
    """Opcion: Buscar productos por nombre"""
    if inventario.esta_vacio():
        print("\nAdvertencia: El inventario esta vacio")
        return

    print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
    nombre_busqueda = leer_texto("Ingrese nombre o parte del nombre: ")
    resultados = inventario.buscar_por_nombre(nombre_busqueda)

    mostrar_lista_productos(resultados)


def menu_mostrar_todos(inventario: Inventario):
    """Opcion: Mostrar todos los productos"""
    if inventario.esta_vacio():
        print("\nEl inventario esta vacio")
        return

    print("\n--- INVENTARIO COMPLETO ---")
    productos = inventario.obtener_todos()
    mostrar_lista_productos(productos)


def mostrar_menu():
    """Muestra el menu principal con opciones formateadas"""
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
    """Funcion principal que ejecuta el ciclo del menu"""
    inventario = Inventario()

    # Datos de ejemplo para pruebas iniciales
    inventario.agregar_producto(Producto(1, "Laptop", 10, 850.00))
    inventario.agregar_producto(Producto(2, "Mouse", 50, 25.50))
    inventario.agregar_producto(Producto(3, "Teclado", 30, 45.00))

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion (1-6): ").strip()

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
            print("\nGracias por usar el sistema de inventarios.\n")
            sys.exit(0)
        else:
            print("\nError: Opcion no valida. Por favor seleccione 1-6")

        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()
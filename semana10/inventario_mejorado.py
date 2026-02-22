import json
import os
from producto_mejorado import Producto
from typing import List, Optional


class Inventario:
    """
    Clase que gestiona una colección de productos con persistencia en archivo de texto.
    Implementa operaciones CRUD con validación de integridad y manejo de excepciones.
    """

    def __init__(self, ruta_archivo: str = "inventario.txt"):
        """Inicializa el inventario y carga los datos desde el archivo"""
        self._productos: List[Producto] = []
        self._ruta_archivo = ruta_archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo de texto/JSON y reconstruye el inventario."""
        try:
            with open(self._ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                for item in datos:
                    producto = Producto(
                        id_producto=item['id'],
                        nombre=item['nombre'],
                        cantidad=item['cantidad'],
                        precio=item['precio']
                    )
                    self._productos.append(producto)
            print(f"--- Sistema: Inventario cargado exitosamente desde '{self._ruta_archivo}' ---")

        except FileNotFoundError:
            print(
                f"--- Sistema: Archivo '{self._ruta_archivo}' no encontrado. Se creará automáticamente al guardar. ---")
            # Creamos un archivo base vacío para asegurar que podemos escribir en el directorio
            try:
                with open(self._ruta_archivo, 'w', encoding='utf-8') as archivo:
                    json.dump([], archivo)
            except PermissionError:
                print("--- Error Crítico: No hay permisos para crear el archivo en este directorio. ---")

        except json.JSONDecodeError:
            print(f"--- Error: El archivo '{self._ruta_archivo}' está corrupto. Se inicia con inventario vacío. ---")

        except PermissionError:
            print(f"--- Error: Permisos insuficientes para leer '{self._ruta_archivo}'. ---")

        except Exception as e:
            print(f"--- Error inesperado al cargar el archivo: {e} ---")

    def guardar_en_archivo(self):
        """Serializa la lista de productos y la guarda en el archivo."""
        try:
            with open(self._ruta_archivo, 'w', encoding='utf-8') as archivo:
                # Utilizamos el método to_dict() de la clase Producto
                datos = [producto.to_dict() for producto in self._productos]
                json.dump(datos, archivo, indent=4)
        except PermissionError:
            # Elevamos el error para que la Interfaz de Usuario lo maneje e informe
            raise PermissionError(f"Permiso denegado para escribir en '{self._ruta_archivo}'")
        except Exception as e:
            raise Exception(f"Fallo inesperado al guardar el archivo: {e}")

    def agregar_producto(self, producto: Producto) -> bool:
        if self.buscar_por_id(producto.id):
            return False

        self._productos.append(producto)
        self.guardar_en_archivo()  # Guardamos cambios en disco
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        producto = self.buscar_por_id(id_producto)
        if producto:
            self._productos.remove(producto)
            self.guardar_en_archivo()  # Guardamos cambios en disco
            return True
        return False

    def actualizar_cantidad(self, id_producto: int, nueva_cantidad: int) -> bool:
        producto = self.buscar_por_id(id_producto)
        if producto:
            producto.cantidad = nueva_cantidad
            self.guardar_en_archivo()  # Guardamos cambios en disco
            return True
        return False

    def actualizar_precio(self, id_producto: int, nuevo_precio: float) -> bool:
        producto = self.buscar_por_id(id_producto)
        if producto:
            producto.precio = nuevo_precio
            self.guardar_en_archivo()  # Guardamos cambios en disco
            return True
        return False

    def buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        for producto in self._productos:
            if producto.id == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, nombre_busqueda: str) -> List[Producto]:
        nombre_normalizado = nombre_busqueda.strip().lower()
        return [
            producto for producto in self._productos
            if nombre_normalizado in producto.nombre.lower()
        ]

    def obtener_todos(self) -> List[Producto]:
        return sorted(self._productos, key=lambda p: p.id)

    def esta_vacio(self) -> bool:
        return len(self._productos) == 0

    def obtener_tamaño(self) -> int:
        return len(self._productos)
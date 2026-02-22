import json
from producto import Producto
from typing import Dict, List, Optional

class Inventario:
    """
    Clase que gestiona una colección de productos con persistencia en archivo JSON.
    Implementa operaciones CRUD optimizadas utilizando un Diccionario.
    """

    def __init__(self, ruta_archivo: str = "inventario.json"):
        """Inicializa el inventario y carga los datos desde el archivo"""
        # Usamos un diccionario (Dict) para búsquedas rápidas usando el ID como llave
        self._productos: Dict[int, Producto] = {}
        self._ruta_archivo = ruta_archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo JSON y reconstruye el inventario en el diccionario."""
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
                    # Almacenamos en el diccionario usando el ID como clave
                    self._productos[producto.id] = producto
            print(f"--- Sistema: Inventario cargado exitosamente desde '{self._ruta_archivo}' ---")

        except FileNotFoundError:
            print(f"--- Sistema: Archivo '{self._ruta_archivo}' no encontrado. Se creará automáticamente al guardar. ---")
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
        """Serializa los valores del diccionario de productos y los guarda en el archivo."""
        try:
            with open(self._ruta_archivo, 'w', encoding='utf-8') as archivo:
                # Iteramos sobre los valores del diccionario para guardarlos
                datos = [producto.to_dict() for producto in self._productos.values()]
                json.dump(datos, archivo, indent=4)
        except PermissionError:
            raise PermissionError(f"Permiso denegado para escribir en '{self._ruta_archivo}'")
        except Exception as e:
            raise Exception(f"Fallo inesperado al guardar el archivo: {e}")

    def agregar_producto(self, producto: Producto) -> bool:
        """Agrega un producto de forma optimizada comprobando la llave en el diccionario."""
        if producto.id in self._productos:
            return False

        self._productos[producto.id] = producto
        self.guardar_en_archivo()
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto instantáneamente si la llave existe."""
        if id_producto in self._productos:
            del self._productos[id_producto]
            self.guardar_en_archivo()
            return True
        return False

    def actualizar_cantidad(self, id_producto: int, nueva_cantidad: int) -> bool:
        producto = self.buscar_por_id(id_producto)
        if producto:
            producto.cantidad = nueva_cantidad
            self.guardar_en_archivo()
            return True
        return False

    def actualizar_precio(self, id_producto: int, nuevo_precio: float) -> bool:
        producto = self.buscar_por_id(id_producto)
        if producto:
            producto.precio = nuevo_precio
            self.guardar_en_archivo()
            return True
        return False

    def buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        """Búsqueda optimizada mediante la llave del diccionario."""
        return self._productos.get(id_producto)

    def buscar_por_nombre(self, nombre_busqueda: str) -> List[Producto]:
        """Búsqueda por nombre recorriendo los valores del diccionario."""
        nombre_normalizado = nombre_busqueda.strip().lower()
        return [
            producto for producto in self._productos.values()
            if nombre_normalizado in producto.nombre.lower()
        ]

    def obtener_todos(self) -> List[Producto]:
        """Retorna todos los productos ordenados por ID."""
        return sorted(self._productos.values(), key=lambda p: p.id)

    def esta_vacio(self) -> bool:
        return len(self._productos) == 0

    def obtener_tamaño(self) -> int:
        return len(self._productos)
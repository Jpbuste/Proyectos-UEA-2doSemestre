from producto import Producto
from typing import List, Optional


class Inventario:
    """
    Clase que gestiona una colección de productos.
    Implementa operaciones CRUD con validación de integridad.
    """

    def __init__(self):
        """Inicializa un inventario vacío"""
        self._productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Añade un nuevo producto al inventario.

        Args:
            producto: Instancia de Producto a agregar

        Returns:
            True si se agregó exitosamente, False si el ID ya existe

        Nota: Verifica unicidad del ID antes de insertar
        """
        if self.buscar_por_id(producto.id):
            return False
        self._productos.append(producto)
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto por su ID.

        Args:
            id_producto: ID del producto a eliminar

        Returns:
            True si se eliminó exitosamente, False si no existe
        """
        producto = self.buscar_por_id(id_producto)
        if producto:
            self._productos.remove(producto)
            return True
        return False

    def actualizar_cantidad(self, id_producto: int, nueva_cantidad: int) -> bool:
        """
        Actualiza la cantidad de un producto existente.

        Args:
            id_producto: ID del producto a actualizar
            nueva_cantidad: Nueva cantidad (no negativa)

        Returns:
            True si se actualizó exitosamente, False si no existe el producto
        """
        producto = self.buscar_por_id(id_producto)
        if producto:
            producto.cantidad = nueva_cantidad
            return True
        return False

    def actualizar_precio(self, id_producto: int, nuevo_precio: float) -> bool:
        """
        Actualiza el precio de un producto existente.

        Args:
            id_producto: ID del producto a actualizar
            nuevo_precio: Nuevo precio (no negativo)

        Returns:
            True si se actualizó exitosamente, False si no existe el producto
        """
        producto = self.buscar_por_id(id_producto)
        if producto:
            producto.precio = nuevo_precio
            return True
        return False

    def buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        """
        Busca un producto por su ID exacto.

        Args:
            id_producto: ID a buscar

        Returns:
            Producto si se encuentra, None en caso contrario
        """
        for producto in self._productos:
            if producto.id == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, nombre_busqueda: str) -> List[Producto]:
        """
        Busca productos cuyo nombre contenga la cadena proporcionada (búsqueda insensible a mayúsculas).

        Args:
            nombre_busqueda: Cadena a buscar dentro de los nombres

        Returns:
            Lista de productos coincidentes (vacía si no hay coincidencias)
        """
        nombre_normalizado = nombre_busqueda.strip().lower()
        return [
            producto for producto in self._productos
            if nombre_normalizado in producto.nombre.lower()
        ]

    def obtener_todos(self) -> List[Producto]:
        """
        Devuelve una copia de la lista completa de productos.

        Returns:
            Lista de productos ordenados por ID
        """
        return sorted(self._productos, key=lambda p: p.id)

    def esta_vacio(self) -> bool:
        """Verifica si el inventario no contiene productos"""
        return len(self._productos) == 0

    def obtener_tamaño(self) -> int:
        """Devuelve la cantidad de productos en el inventario"""
        return len(self._productos)
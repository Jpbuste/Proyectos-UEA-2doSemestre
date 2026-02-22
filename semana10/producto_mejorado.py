class Producto:
    """
    Clase que representa un producto en el inventario.
    Atributos con validación para garantizar integridad de datos.
    """

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.

        Args:
            id_producto: Identificador único del producto (entero positivo)
            nombre: Nombre descriptivo del producto (mínimo 1 carácter)
            cantidad: Cantidad disponible en inventario (entero no negativo)
            precio: Precio unitario del producto (float positivo)

        Raises:
            ValueError: Si los parámetros no cumplen con las validaciones
        """
        if id_producto <= 0:
            raise ValueError("El ID debe ser un número positivo")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self._id = id_producto
        self._nombre = nombre.strip()
        self._cantidad = cantidad
        self._precio = round(precio, 2)  # Precisión de 2 decimales para moneda

    # Getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio(self) -> float:
        return self._precio

    # Setters con validación
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nuevo_nombre.strip()

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = round(nuevo_precio, 2)

    def __str__(self) -> str:
        """Representación en cadena para visualización amigable"""
        return (f"ID: {self._id:4d} | Nombre: {self._nombre:<20} | "
                f"Cantidad: {self._cantidad:4d} | Precio: ${self._precio:7.2f}")

    def to_dict(self) -> dict:
        """Conversión a diccionario para serialización en archivo JSON"""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }
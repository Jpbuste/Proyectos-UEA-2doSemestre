# Programa: Conversión de unidades de temperatura
# Funcionalidad: Permite al usuario convertir grados Celsius a Fahrenheit y Kelvin,
#                con validación de entrada y verificación del cero absoluto.
# Tipos de datos utilizados: int, float, str, bool
# Convenciones: snake_case, type hints, constantes en mayúsculas
# Autor: Jhon Michael Panta Buste
# Fecha: 11 de enero de 2026

# Constantes físicas
CERO_ABSOLUTO_CELSIUS: float = -273.15  # Temperatura mínima posible en °C


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte una temperatura en grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


def celsius_a_kelvin(celsius: float) -> float:
    """Convierte una temperatura en grados Celsius a Kelvin."""
    return celsius - CERO_ABSOLUTO_CELSIUS  # Equivalente a celsius + 273.15


def obtener_temperatura_valida() -> float:
    """
    Solicita al usuario una temperatura en Celsius y valida que sea un número.
    Repite hasta que se ingrese un valor numérico válido.
    """
    while True:
        entrada_usuario: str = input("Ingrese la temperatura en grados Celsius: ").strip()
        try:
            return float(entrada_usuario)
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número (ej. -10, 25.5).")


def es_temperatura_fisicamente_posible(celsius: float) -> bool:
    """Verifica si la temperatura está por encima o en el cero absoluto."""
    return celsius >= CERO_ABSOLUTO_CELSIUS


def main() -> None:
    """Función principal que orquesta la ejecución del programa."""
    print("🌡️  Conversor de Temperatura: Celsius → Fahrenheit y Kelvin")
    print("-" * 60)

    # Obtener entrada segura del usuario
    temperatura_celsius: float = obtener_temperatura_valida()

    # Realizar conversiones
    temp_fahrenheit: float = celsius_a_fahrenheit(temperatura_celsius)
    temp_kelvin: float = celsius_a_kelvin(temperatura_celsius)

    # Evaluar validez física
    es_valida: bool = es_temperatura_fisicamente_posible(temperatura_celsius)

    # Mostrar resultados
    print("\n✅ Resultados:")
    print(f"• Celsius:    {temperatura_celsius:.2f} °C")
    print(f"• Fahrenheit: {temp_fahrenheit:.2f} °F")
    print(f"• Kelvin:     {temp_kelvin:.2f} K")

    if not es_valida:
        print("\n⚠️  Advertencia: La temperatura ingresada está por debajo del cero absoluto.")
        print("   Esto no es físicamente posible en la naturaleza.")


if __name__ == "__main__":
    main()
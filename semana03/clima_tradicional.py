# clima_tradicional.py
# Implementación del cálculo del promedio semanal de temperaturas usando programación tradicional (estructurada).

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de una semana (7 días).
    Retorna una lista con las 7 temperaturas ingresadas.
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("=== Ingreso de temperaturas semanales (°C) ===")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Parámetro:
        temperaturas (list): lista de números (float o int).
    Retorna:
        float: promedio de las temperaturas.
    """
    if not temperaturas:
        return 0.0
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que orquesta la entrada de datos y el cálculo del promedio.
    """
    print("Programación Tradicional: Promedio Semanal del Clima\n")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\n🌡️  El promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
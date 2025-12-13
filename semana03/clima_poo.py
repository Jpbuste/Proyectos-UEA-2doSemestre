# clima_poo.py
# Implementación del cálculo del promedio semanal de temperaturas usando Programación Orientada a Objetos (POO).

class ClimaSemanal:
    """
    Clase que representa el clima semanal.
    Encapsula los datos (lista de temperaturas) y las operaciones relacionadas.
    """
    
    def __init__(self):
        # Atributo privado para almacenar temperaturas (encapsulamiento)
        self.__temperaturas = []
        self.__dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_temperaturas(self):
        """
        Solicita al usuario las temperaturas diarias y las almacena en el atributo privado.
        Aplica validación de entrada.
        """
        print("=== Ingreso de temperaturas semanales (°C) ===")
        for dia in self.__dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia}: "))
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

    def obtener_promedio(self):
        """
        Calcula y retorna el promedio de las temperaturas almacenadas.
        Retorna:
            float: promedio de las temperaturas, o 0.0 si no hay datos.
        """
        if not self.__temperaturas:
            return 0.0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_resultado(self):
        """
        Muestra el promedio semanal con formato amigable.
        """
        promedio = self.obtener_promedio()
        print(f"\n🌡️  El promedio semanal de temperatura es: {promedio:.2f} °C")


# Opcional: Ejemplo de herencia y polimorfismo (mejora conceptual, no obligatoria pero válida)
class ClimaSemanalConUmbral(ClimaSemanal):
    """
    Subclase que extiende ClimaSemanal para agregar funcionalidad adicional:
    evaluar si alguna temperatura supera un umbral definido.
    Ejemplifica herencia y polimorfismo (sobrescritura de método mostrar_resultado).
    """
    
    def __init__(self, umbral=30.0):
        super().__init__()  # Llama al constructor de la clase base
        self.umbral = umbral  # Umbral de alerta (atributo adicional)

    def hay_temperatura_alta(self):
        """Retorna True si alguna temperatura ≥ umbral."""
        return any(temp >= self.umbral for temp in self._ClimaSemanal__temperaturas)

    def mostrar_resultado(self):
        """
        Método sobrescrito (polimorfismo): muestra el promedio y una alerta si aplica.
        """
        super().mostrar_resultado()  # Reutiliza la lógica base
        if self.hay_temperatura_alta():
            print(f"⚠️  Alerta: Al menos una temperatura superó el umbral de {self.umbral} °C.")
        else:
            print(f"✅  Todas las temperaturas están por debajo de {self.umbral} °C.")


def main():
    """
    Función principal para demostrar el uso de la clase (y opcionalmente la subclase).
    """
    print("Programación Orientada a Objetos: Promedio Semanal del Clima\n")
    
    # Uso de la clase base
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_resultado()

    # Opcional: descomentar para usar versión con umbral (herencia + polimorfismo)
    # print("\n--- Versión con umbral de alerta (30°C) ---")
    # clima_umbral = ClimaSemanalConUmbral(umbral=30.0)
    # clima_umbral.ingresar_temperaturas()
    # clima_umbral.mostrar_resultado()


if __name__ == "__main__":
    main()
"""
2_sistema_parqueaderos.py
Modela un parqueadero automatizado con clases: Vehiculo, Espacio, Parqueadero.
Incluye tipologías de espacios y cálculo dinámico de tarifas.
"""

class Vehiculo:
    """Representa un vehículo ingresado al parqueadero."""
    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo  # "Automóvil", "Motocicleta", "Bicicleta"
        self.hora_entrada = None

    def registrar_entrada(self):
        from datetime import datetime
        self.hora_entrada = datetime.now()


class Espacio:
    """Representa un espacio físico numerado y tipificado."""
    def __init__(self, numero, tipo_permitido):
        self.numero = numero
        self.tipo_permitido = tipo_permitido  # "Automóvil", "Motocicleta", "Universal"
        self.ocupado = False
        self.vehiculo = None

    def ocupar(self, vehiculo):
        if not self.ocupado and (self.tipo_permitido == "Universal" or self.tipo_permitido == vehiculo.tipo):
            self.vehiculo = vehiculo
            self.ocupado = True
            vehiculo.registrar_entrada()
            return True
        return False

    def liberar(self):
        if self.ocupado:
            self.vehiculo = None
            self.ocupado = False


class Parqueadero:
    """Gestiona una colección de espacios y cálculo de tarifas."""
    TARIFAS = {
        "Automóvil": 2.0,    # $/hora
        "Motocicleta": 1.0,
        "Bicicleta": 0.5
    }

    def __init__(self, nombre):
        self.nombre = nombre
        self.espacios = []

    def agregar_espacio(self, espacio):
        self.espacios.append(espacio)

    def buscar_espacio_disponible(self, tipo_vehiculo):
        for e in self.espacios:
            if not e.ocupado and (e.tipo_permitido == "Universal" or e.tipo_permitido == tipo_vehiculo):
                return e
        return None

    def calcular_tarifa(self, vehiculo, horas=None):
        from datetime import datetime
        if vehiculo.hora_entrada is None:
            return 0.0
        if horas is None:
            delta = datetime.now() - vehiculo.hora_entrada
            horas = delta.total_seconds() / 3600
        tarifa_hora = self.TARIFAS.get(vehiculo.tipo, 0)
        return round(tarifa_hora * max(horas, 0.5), 2)  # Mínimo 0.5 horas


# === Ejemplo de uso ===
if __name__ == "__main__":
    centro = Parqueadero("Plaza Mayor")
    centro.agregar_espacio(Espacio(101, "Automóvil"))
    centro.agregar_espacio(Espacio(201, "Motocicleta"))

    auto = Vehiculo("ABC-123", "Automóvil")
    espacio = centro.buscar_espacio_disponible("Automóvil")
    if espacio and espacio.ocupar(auto):
        print(f"✓ {auto.placa} estacionado en espacio {espacio.numero}")
        print(f"Tarifa estimada (2h): ${centro.calcular_tarifa(auto, 2)}")
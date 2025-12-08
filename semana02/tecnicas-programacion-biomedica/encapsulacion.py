# ============================================
#     ENCAPSULAMIENTO: Sensor de Frecuencia Cardíaca
# ============================================
# Se implementa una clase que protege sus datos internos mediante
# atributos privados y propiedades controladas, asegurando que
# solo se acepten valores válidos desde el punto de vista clínico.

class SensorPulso:
    """Sensor biomédico que monitorea frecuencia cardíaca con acceso controlado."""
    
    def __init__(self, id_sensor):
        self.id_sensor = id_sensor
        self._frecuencia = 0
        self._conectado = False

    @property
    def frecuencia(self):
        """Devuelve la frecuencia actual si el sensor está conectado; None en caso contrario."""
        return self._frecuencia if self._conectado else None

    @frecuencia.setter
    def frecuencia(self, valor):
        """Asigna un nuevo valor solo si está conectado y dentro del rango clínico."""
        if not self._conectado:
            raise PermissionError("Error: el sensor debe estar conectado para actualizar la frecuencia.")
        if isinstance(valor, (int, float)) and 30 <= valor <= 220:
            self._frecuencia = round(valor)
        else:
            raise ValueError("Valor inválido: la frecuencia cardíaca debe estar entre 30 y 220 bpm.")

    @property
    def conectado(self):
        return self._conectado

    def conectar(self):
        """Establece conexión con el sistema de monitoreo."""
        self._conectado = True
        return f"🔌 Sensor {self.id_sensor} conectado."

    def desconectar(self):
        """Finaliza la conexión y reinicia los valores."""
        self._conectado = False
        self._frecuencia = 0
        return f"🔌 Sensor {self.id_sensor} desconectado."


# --- Programa principal ---
if __name__ == "__main__":
    print("✅ Ejemplo de ENCAPSULAMIENTO en sensores clínicos")
    
    sensor = SensorPulso("SP-789")
    print(sensor.conectar())
    
    try:
        sensor.frecuencia = 75
        print(f"✔️ Lectura válida: {sensor.frecuencia} bpm")
        
        sensor.frecuencia = 250  # Esto lanzará excepción
    except ValueError as e:
        print(f"❌ Error capturado: {e}")
    
    print(sensor.desconectar())
    print(f"➡️ Intento de lectura tras desconexión: {sensor.frecuencia}")
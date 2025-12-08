# ============================================
#     HERENCIA: Especialización de Equipos Clínicos
# ============================================
# Se define una clase base con comportamiento común, y subclases
# que heredan y extienden funcionalidades para casos específicos.
# Esto evita duplicación y mejora la mantenibilidad del código.

class EquipoClinico:
    """Clase base para equipos utilizados en entornos médicos."""
    
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante
        self._estado = "inactivo"

    def activar(self):
        self._estado = "activo"
        return f"🟢 {self.modelo} activado."

    def desactivar(self):
        self._estado = "inactivo"
        return f"⚪ {self.modelo} desactivado."

    def estado_actual(self):
        return f"Estado actual: {self._estado}"


class RobotCirujano(EquipoClinico):
    """Subclase especializada: robot para cirugía mínimamente invasiva."""
    
    def __init__(self, modelo, fabricante, precision_mm=0.1):
        super().__init__(modelo, fabricante)
        self.precision_mm = precision_mm
        self._instrumentos = ["bisturí", "pinza", "cauterizador"]

    def seleccionar_instrumento(self, nombre):
        if nombre in self._instrumentos:
            return f"🔧 Instrumento '{nombre}' acoplado con precisión ±{self.precision_mm} mm."
        return f"❌ Instrumento '{nombre}' no disponible."


class MonitorPaciente(EquipoClinico):
    """Subclase especializada: monitorización continua de signos vitales."""
    
    def __init__(self, modelo, fabricante, sensores=None):
        super().__init__(modelo, fabricante)
        self.sensores = sensores or ["ECG", "SpO₂", "TA"]

    def registrar_dato(self, tipo, valor):
        if tipo in self.sensores:
            return f"📈 {tipo}: {valor} registrado."
        return f"⚠️ Sensor {tipo} no configurado en este modelo."


# --- Programa principal ---
if __name__ == "__main__":
    print("✅ Ejemplo de HERENCIA en equipos biomédicos")
    
    robot = RobotCirujano("DaVinci-S", "Intuitive Surgical", 0.05)
    monitor = MonitorPaciente("VitalTrack Pro", "Medtronic", ["ECG", "Temp", "Resp"])

    print(robot.activar())
    print(robot.seleccionar_instrumento("bisturí"))
    print(robot.estado_actual())

    print("\n" + monitor.activar())
    print(monitor.registrar_dato("ECG", "78 bpm"))
    print(monitor.estado_actual())
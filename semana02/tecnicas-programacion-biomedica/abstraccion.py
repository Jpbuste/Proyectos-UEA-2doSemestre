# ============================================
#     ABSTRACCIÓN: Dispositivo Médico
# ============================================
# Se define una clase abstracta que captura lo esencial de cualquier
# dispositivo biomédico: identificación, tipo y comportamiento básico.
# La abstracción permite trabajar con conceptos generales sin conocer
# implementaciones concretas, facilitando el diseño modular.

from abc import ABC, abstractmethod

class DispositivoMedico(ABC):
    """Clase abstracta que representa la interfaz esencial de un dispositivo biomédico."""
    
    def __init__(self, id_equipo, tipo):
        self.id_equipo = id_equipo
        self.tipo = tipo
        self._estado = "apagado"  # estado interno protegido

    @abstractmethod
    def iniciar_diagnostico(self):
        """Método abstracto: cada dispositivo debe definir su propio protocolo."""
        pass

    def encender(self):
        """Método concreto compartido: transición controlada a estado 'encendido'."""
        if self._estado == "apagado":
            self._estado = "encendido"
            return f"⚡ {self.tipo} (ID: {self.id_equipo}) encendido."
        return f"⚠️ {self.tipo} ya está encendido."

    def apagar(self):
        """Apagado seguro: detiene operaciones antes de cambiar estado."""
        if self._estado == "encendido":
            self._estado = "apagado"
            return f"🛑 {self.tipo} (ID: {self.id_equipo}) apagado."
        return f"ℹ️ {self.tipo} ya está apagado."


# --- Ejemplo de subclase concreta (para demostrar funcionalidad) ---
class MonitorECG(DispositivoMedico):
    def iniciar_diagnostico(self):
        return f"📊 Iniciando diagnóstico con {self.tipo} (ID: {self.id_equipo}): análisis de ritmo cardíaco en curso..."


# --- Programa principal (solo para demostración) ---
if __name__ == "__main__":
    print("✅ Ejemplo de ABSTRACCIÓN en sistemas biomédicos")
    print("   Clase abstracta 'DispositivoMedico' definida.")
    
    # Instancia de una subclase concreta
    ecg = MonitorECG("ECG-2025", "Monitor de Electrocardiograma")
    print(ecg.encender())
    print(ecg.iniciar_diagnostico())
    print(ecg.apagar())
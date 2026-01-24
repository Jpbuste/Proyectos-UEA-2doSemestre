# historial_clinico.py
# Ejemplo académico en el contexto de salud: uso de constructores y destructores.
# Autor: Jhon Michael Panta Buste
# Asignatura: Programación Orientada a Objetos – Enfermería en Urgencias y Emergencias

class HistorialClinicoTemporal:
    """
    Clase que representa un historial clínico temporal utilizado durante una
    atención de emergencia. Simula la apertura de un expediente al inicio
    de la consulta y su cierre controlado al finalizar.
    """

    def __init__(self, nombre_paciente: str, id_paciente: str, triaje: str):
        """
        Constructor de la clase.
        Se ejecuta al crear una instancia del historial clínico.
        Inicializa los datos esenciales del paciente y registra la apertura
        del expediente en consola (simulando un sistema real).
        """
        self.nombre_paciente = nombre_paciente
        self.id_paciente = id_paciente
        self.triaje = triaje  # Ej.: 'Rojo', 'Amarillo', 'Verde'
        print(f"[+] Expediente clínico abierto para: {self.nombre_paciente} (ID: {self.id_paciente})")
        print(f"    Nivel de triaje asignado: {self.triaje.upper()}")

    def __del__(self):
        """
        Destructor de la clase.
        Se invoca automáticamente cuando el objeto es eliminado.
        Simula el cierre seguro del historial clínico (ej.: liberación de recursos,
        notificación de finalización de atención, respaldo temporal, etc.).
        """
        print(f"[-] Expediente clínico de {self.nombre_paciente} ha sido cerrado y recursos liberados.")


def main():
    """
    Función principal que simula la atención de dos pacientes en urgencias.
    """
    print("=== Sistema de Gestión de Historiales Clínicos Temporales ===\n")

    # Atención del primer paciente
    paciente1 = HistorialClinicoTemporal("María López", "P-2026-001", "Rojo")

    # Atención del segundo paciente
    paciente2 = HistorialClinicoTemporal("Carlos Méndez", "P-2026-002", "Amarillo")

    print("\n[...] Registrando signos vitales y evolución clínica...\n")

    # Finalización de la atención → liberación explícita de recursos
    del paciente1
    del paciente2

    print("Atención de emergencia finalizada. Sistema listo para nuevos casos.\n")


if __name__ == "__main__":
    main()
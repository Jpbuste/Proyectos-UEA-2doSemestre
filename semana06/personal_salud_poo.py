# =============================================================
# Tarea: Aplicación de Conceptos de POO en Python
# Autor: Jhon Michael Panta Buste
# Descripción: Modelado de personal de salud usando POO en Python
# =============================================================

# ----------------------------
# Clase Base: PersonalSalud
# ----------------------------
class PersonalSalud:
    """
    Clase base que representa a cualquier profesional de la salud.
    Incluye atributos comunes y métodos genéricos.
    """

    def __init__(self, nombre, identificacion, especialidad):
        """
        Constructor de la clase base.
        :param nombre: Nombre completo del profesional (str)
        :param identificacion: Número o código de identificación (str)
        :param especialidad: Área de especialización (str)
        """
        self.nombre = nombre                  # Atributo público
        self._identificacion = identificacion  # Atributo protegido (encapsulación parcial)
        self.__especialidad = especialidad     # Atributo privado (encapsulación fuerte)

    def atender_paciente(self):
        """
        Método genérico que será sobrescrito por subclases.
        Ilustra polimorfismo.
        """
        raise NotImplementedError("Este método debe implementarse en una subclase.")

    def obtener_info(self):
        """
        Retorna información básica del profesional.
        """
        return f"Nombre: {self.nombre} | ID: {self._identificacion}"

    # Getters y setters para el atributo privado
    def get_especialidad(self):
        """Permite acceder de forma controlada a la especialidad."""
        return self.__especialidad

    def set_especialidad(self, nueva_especialidad):
        """Permite modificar la especialidad con validación."""
        if isinstance(nueva_especialidad, str) and nueva_especialidad.strip():
            self.__especialidad = nueva_especialidad
        else:
            raise ValueError("La especialidad debe ser una cadena no vacía.")


# ----------------------------
# Clase Derivada: Enfermero
# ----------------------------
class Enfermero(PersonalSalud):
    """
    Clase derivada que representa a un enfermero/a.
    Hereda de PersonalSalud y añade funcionalidad específica.
    """

    def __init__(self, nombre, identificacion, especialidad, turno):
        super().__init__(nombre, identificacion, especialidad)
        self.__turno = turno  # Turno de trabajo: "mañana", "tarde", "noche"

    def atender_paciente(self):
        """
        Sobrescribe el método de la clase base.
        Ejemplo de polimorfismo: mismo método, comportamiento específico.
        """
        return f"{self.nombre} está realizando cuidados básicos y monitoreo vital."

    def get_turno(self):
        return self.__turno


# ----------------------------
# Clase Derivada: Medico
# ----------------------------
class Medico(PersonalSalud):
    """
    Otra subclase: médico/a.
    También demuestra herencia y polimorfismo.
    """

    def __init__(self, nombre, identificacion, especialidad, colegiado):
        super().__init__(nombre, identificacion, especialidad)
        self.__colegiado = colegiado  # Número de colegiatura profesional

    def atender_paciente(self):
        """
        Implementación específica del método polimórfico.
        """
        return f"{self.nombre} está diagnosticando y prescribiendo tratamiento."

    def get_colegiado(self):
        return self.__colegiado


# ----------------------------
# Función Polimórfica
# ----------------------------
def gestionar_atencion(profesional):
    """
    Función que acepta cualquier objeto derivado de PersonalSalud.
    Demuestra polimorfismo en tiempo de ejecución.
    """
    print(f"[INFO] {profesional.obtener_info()}")
    print(f"[ATENCIÓN] {profesional.atender_paciente()}")
    print(f"[ESPECIALIDAD] {profesional.get_especialidad()}")
    print("-" * 50)


# ----------------------------
# Bloque principal del programa
# ----------------------------
if __name__ == "__main__":
    # Creación de instancias (objetos)
    enfermero_urgencias = Enfermero(
        nombre="Ana López",
        identificacion="ENF-2023-045",
        especialidad="Urgencias",
        turno="noche"
    )

    medico_traumatologia = Medico(
        nombre="Dr. Carlos Mena",
        identificacion="MED-2018-112",
        especialidad="Traumatología",
        colegiado="COL-88765"
    )

    # Demostración de los conceptos de POO
    print("=== Sistema de Gestión de Personal de Salud ===\n")

    # Polimorfismo: misma función, comportamiento distinto según el objeto
    gestionar_atencion(enfermero_urgencias)
    gestionar_atencion(medico_traumatologia)

    # Acceso controlado a atributos encapsulados
    print(f"Turno del enfermero: {enfermero_urgencias.get_turno()}")
    print(f"Colegiatura del médico: {medico_traumatologia.get_colegiado()}")

    # Modificación segura de especialidad
    enfermero_urgencias.set_especialidad("Cuidados Intensivos")
    print(f"Nueva especialidad del enfermero: {enfermero_urgencias.get_especialidad()}")
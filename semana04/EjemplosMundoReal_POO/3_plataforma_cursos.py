"""
3_plataforma_cursos.py
Modela una plataforma de aprendizaje con: Curso, Estudiante, Leccion, Progreso.
Incluye seguimiento de avance y certificación.
"""

class Leccion:
    def __init__(self, titulo, duracion_min, contenido):
        self.titulo = titulo
        self.duracion_min = duracion_min
        self.contenido = contenido
        self.completada = False

    def marcar_completada(self):
        self.completada = True


class Curso:
    def __init__(self, codigo, nombre, nivel):
        self.codigo = codigo
        self.nombre = nombre
        self.nivel = nivel  # "Básico", "Intermedio", "Avanzado"
        self.lecciones = []
        self.estudiantes = []

    def agregar_leccion(self, leccion):
        self.lecciones.append(leccion)

    def inscribir_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            estudiante.cursos_inscritos.append(self)

    def porcentaje_avance(self, estudiante):
        """Calcula el porcentaje de avance de un estudiante en este curso."""
        if not self.lecciones:
            return 100.0
        # Obtener las lecciones completadas por este estudiante en este curso
        progreso = estudiante.progreso.get(self.codigo, [])
        completadas = sum(1 for leccion in self.lecciones if leccion in progreso and leccion.completada)
        return round((completadas / len(self.lecciones)) * 100, 1)


class Estudiante:
    def __init__(self, id_est, nombre):
        self.id = id_est
        self.nombre = nombre
        self.cursos_inscritos = []
        self.progreso = {}  # {codigo_curso: [leccion1, leccion2, ...]}

    def completar_leccion(self, curso, leccion):
        """Registra que el estudiante ha completado una lección de un curso."""
        if curso not in self.cursos_inscritos:
            raise ValueError("El estudiante no está inscrito en este curso.")
        if curso.codigo not in self.progreso:
            self.progreso[curso.codigo] = []
        if leccion not in self.progreso[curso.codigo]:
            self.progreso[curso.codigo].append(leccion)
        leccion.marcar_completada()

    def esta_certificado(self, curso):
        """Verifica si el estudiante alcanzó al menos el 80% de avance."""
        return self.porcentaje_avance_en_curso(curso) >= 80.0

    def porcentaje_avance_en_curso(self, curso):
        """Delega el cálculo al curso para mayor cohesión."""
        return curso.porcentaje_avance(self)


# === Ejemplo de uso ===
if __name__ == "__main__":
    # Crear curso y lecciones
    curso_py = Curso("PY-101", "Fundamentos de Python", "Básico")
    curso_py.agregar_leccion(Leccion("Sintaxis Básica", 30, "print(), variables, tipos de datos"))
    curso_py.agregar_leccion(Leccion("Estructuras de Control", 45, "if, for, while, break"))

    # Crear estudiante e inscribirlo
    est = Estudiante("E-77", "Carla Rojas")
    curso_py.inscribir_estudiante(est)

    # Completar primera lección
    est.completar_leccion(curso_py, curso_py.lecciones[0])

    # Mostrar avance (¡corregido! → ahora se llama desde el curso o desde el estudiante con delegación)
    print(f"✅ Estudiante: {est.nombre}")
    print(f"📚 Curso: {curso_py.nombre}")
    print(f"📊 Avance: {curso_py.porcentaje_avance(est)}%")  # Forma directa
    # Alternativa (usando el método delegado en Estudiante):
    # print(f"📊 Avance: {est.porcentaje_avance_en_curso(curso_py)}%")

    # Verificar certificación
    print(f"🎓 ¿Certificado? {'Sí' if est.esta_certificado(curso_py) else 'No'}")

    # Completar segunda lección y volver a verificar
    est.completar_leccion(curso_py, curso_py.lecciones[1])
    print("\n➡️  Después de completar todas las lecciones:")
    print(f"📊 Avance: {curso_py.porcentaje_avance(est)}%")
    print(f"🎓 ¿Certificado? {'Sí' if est.esta_certificado(curso_py) else 'No'}")
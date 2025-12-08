# ============================================
#     POLIMORFISMO: Protocolos Clínicos
# ============================================
# Varias clases diferentes implementan el mismo método 'ejecutar_protocolo()',
# pero con comportamientos específicos. Una función externa puede usarlos
# indistintamente, sin conocer su tipo concreto.

class ProtocoloMedico:
    """Clase base (para coherencia conceptual); no es obligatoria por duck typing."""
    def ejecutar_protocolo(self):
        raise NotImplementedError("Debe implementarse en subclases.")


class ProtocoloDesinfeccion(ProtocoloMedico):
    def __init__(self, superficie):
        self.superficie = superficie

    def ejecutar_protocolo(self):
        return f"🧴 Protocolo de desinfección: aplicación en {self.superficie} durante 10 minutos."


class ProtocoloReanimacion(ProtocoloMedico):
    def __init__(self, compresiones_por_minuto=100):
        self.comp_min = compresiones_por_minuto

    def ejecutar_protocolo(self):
        return f"🆘 Protocolo de RCP: {self.comp_min} compresiones/min + 2 ventilaciones cada 30 compresiones."


class ProtocoloCalibracion(ProtocoloMedico):
    def __init__(self, equipo):
        self.equipo = equipo

    def ejecutar_protocolo(self):
        return f"⚙️ Protocolo de calibración: verificación y ajuste automático en {self.equipo} completado."


def ejecutar_protocolo_unificado(proto):
    """Función polimórfica: recibe cualquier objeto con método 'ejecutar_protocolo()'."""
    print("▶️ Iniciando protocolo estándar...")
    resultado = proto.ejecutar_protocolo()
    print(resultado)
    print("✅ Protocolo finalizado.\n")


# --- Programa principal ---
if __name__ == "__main__":
    print("✅ Ejemplo de POLIMORFISMO en procedimientos clínicos")
    
    protocolos = [
        ProtocoloDesinfeccion("mesa quirúrgica"),
        ProtocoloReanimacion(110),
        ProtocoloCalibracion("Monitor Multifuncional M7")
    ]

    for p in protocolos:
        ejecutar_protocolo_unificado(p)
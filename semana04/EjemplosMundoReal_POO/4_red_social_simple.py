"""
4_red_social_simple.py
Modela una red social básica con clases: Usuario, Publicacion, Comentario.
Demuestra interacción entre objetos, relaciones de seguimiento y control de visibilidad.
"""

class Usuario:
    """Representa a un usuario registrado en la red social."""
    def __init__(self, nombre_usuario, nombre_real):
        self.nombre_usuario = nombre_usuario
        self.nombre_real = nombre_real
        self.publicaciones = []      # Lista de objetos Publicacion
        self.seguidores = []         # Lista de objetos Usuario que lo siguen
        self.siguiendo = []          # Lista de objetos Usuario que sigue

    def seguir(self, otro_usuario):
        """Establece una relación de seguimiento (unidireccional)."""
        if otro_usuario not in self.siguiendo:
            self.siguiendo.append(otro_usuario)
            otro_usuario.seguidores.append(self)

    def dejar_de_seguir(self, otro_usuario):
        """Termina una relación de seguimiento."""
        if otro_usuario in self.siguiendo:
            self.siguiendo.remove(otro_usuario)
            otro_usuario.seguidores.remove(self)

    def publicar(self, contenido, es_privado=False):
        """Crea una nueva publicación y la añade al historial."""
        pub = Publicacion(self, contenido, es_privado)
        self.publicaciones.append(pub)
        return pub

    def feed(self, incluir_privadas=False):
        """Genera un 'feed' con publicaciones de quienes sigue (y las propias)."""
        feed = []
        # Incluir publicaciones propias
        feed.extend(self.publicaciones)
        # Incluir publicaciones de quienes sigue
        for seguido in self.siguiendo:
            for pub in seguido.publicaciones:
                if incluir_privadas or pub.visible_para(self):
                    feed.append(pub)
        # Ordenar por recencia (simulado: las más nuevas al final)
        return feed

    def __str__(self):
        return f"@{self.nombre_usuario} ({self.nombre_real})"


class Publicacion:
    """Representa una publicación (texto) realizada por un usuario."""
    def __init__(self, autor, contenido, es_privado=False):
        self.autor = autor
        self.contenido = contenido
        self.es_privado = es_privado
        self.comentarios = []       # Lista de objetos Comentario
        self.me_gusta = 0

    def dar_like(self):
        """Incrementa el contador de 'me gusta'."""
        self.me_gusta += 1

    def comentar(self, usuario, texto):
        """Añade un comentario hecho por un usuario."""
        comentario = Comentario(usuario, texto)
        self.comentarios.append(comentario)
        return comentario

    def visible_para(self, usuario):
        """Determina si la publicación es visible para un usuario dado."""
        # Si es pública → siempre visible
        if not self.es_privado:
            return True
        # Si es privada → solo visible para el autor o sus seguidores
        return usuario == self.autor or usuario in self.autor.seguidores

    def __str__(self):
        visibilidad = "🔒 Privada" if self.es_privado else "🌐 Pública"
        return f"[{visibilidad}] {self.autor.nombre_usuario}: '{self.contenido}' ({self.me_gusta} ❤️)"


class Comentario:
    """Representa un comentario en una publicación."""
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto

    def __str__(self):
        return f"  ↳ {self.autor.nombre_usuario}: \"{self.texto}\""


# === Ejemplo de uso ===
if __name__ == "__main__":
    # Crear usuarios
    sofia = Usuario("viajero88", "Sofía Méndez")
    luis = Usuario("fotomaniaco", "Luis Castro")
    ana = Usuario("lectora_curiosa", "Ana Torres")

    # Relaciones de seguimiento
    sofia.seguir(luis)      # Sofía sigue a Luis
    ana.seguir(sofia)       # Ana sigue a Sofía
    ana.seguir(luis)        # Ana sigue a Luis

    # Publicaciones
    pub1 = luis.publicar("Atardecer en los Andes 🌄", es_privado=False)
    pub2 = sofia.publicar("Nuevo libro de ciencia ficción 🔭", es_privado=True)  # Solo seguidores
    pub3 = luis.publicar("Detrás de escena: edición de fotos 📸", es_privado=True)

    # Interacciones
    pub1.dar_like()
    pub1.dar_like()
    comentario1 = pub1.comentar(sofia, "¡Increíble toma! ¿Dónde fue exactamente?")
    pub1.comentar(ana, "Los colores son espectaculares 👏")

    # Mostrar resultados
    print("✅ Usuarios creados:")
    print(f"  • {sofia} → sigue a {len(sofia.siguiendo)} usuario(s)")
    print(f"  • {luis} → tiene {len(luis.seguidores)} seguidor(es)")
    print()

    print("📝 Publicaciones de Luis:")
    for p in luis.publicaciones:
        print(p)
        for c in p.comentarios:
            print(c)
    print()

    print("📡 Feed de Ana (incluye lo que publican quienes sigue):")
    for p in ana.feed():
        print(f"  {p}")
    print()

    print("👀 ¿Ana puede ver la publicación privada de Sofía?")
    puede_ver = pub2.visible_para(ana)
    print(f"  → {'Sí' if puede_ver else 'No'} (Ana sigue a Sofía)")
    
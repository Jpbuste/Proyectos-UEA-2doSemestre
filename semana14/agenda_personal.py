import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaPersonalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")
        self.root.geometry("750x550")

        # --- PALETA DE COLORES MINIMALISTA ---
        self.bg_color = "#F4F6F9"  # Fondo general claro y moderno
        self.card_color = "#FFFFFF"  # Fondo blanco para contenedores
        self.text_color = "#333333"  # Texto oscuro suave
        self.btn_add_color = "#4A90E2"  # Azul moderno
        self.btn_del_color = "#E74C3C"  # Rojo suave
        self.btn_exit_color = "#95A5A6"  # Gris neutro

        self.root.configure(bg=self.bg_color)

        # --- ESTILOS AVANZADOS (ttk.Style) ---
        style = ttk.Style()
        # 'clam' es un tema base más plano, ideal para Linux y diseños modernos
        style.theme_use("clam")

        # Estilo para el Treeview (Tabla)
        style.configure("Treeview",
                        background=self.card_color,
                        foreground=self.text_color,
                        rowheight=30,  # Filas más altas para que respire
                        fieldbackground=self.card_color,
                        font=("Helvetica", 10))

        # Estilo para los encabezados de la tabla
        style.configure("Treeview.Heading",
                        font=("Helvetica", 10, "bold"),
                        background="#E1E8ED",
                        foreground=self.text_color)

        # Quitar los bordes feos al seleccionar
        style.map('Treeview', background=[('selected', '#D6EAF8')])

        # --- ORGANIZACIÓN CON CONTENEDORES (FRAMES) ---
        # Se usa un padding mayor para dar estilo minimalista
        self.frame_entrada = tk.Frame(self.root, bg=self.card_color, padx=20, pady=20, bd=0)
        self.frame_entrada.pack(fill="x", padx=20, pady=(20, 10))

        self.frame_botones = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=5)
        self.frame_botones.pack(fill="x", padx=20)

        self.frame_lista = tk.Frame(self.root, bg=self.card_color, padx=10, pady=10)
        self.frame_lista.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        # --- COMPONENTES DEL FRAME DE ENTRADA ---
        fuente_labels = ("Helvetica", 10, "bold")

        # Fecha
        tk.Label(self.frame_entrada, text="Fecha:", bg=self.card_color, fg=self.text_color, font=fuente_labels).grid(
            row=0, column=0, sticky="w", pady=5)
        self.entrada_fecha = DateEntry(self.frame_entrada, width=15, background=self.btn_add_color, foreground='white',
                                       borderwidth=0, date_pattern='dd/mm/yyyy', font=("Helvetica", 10))
        self.entrada_fecha.grid(row=0, column=1, padx=(10, 20), pady=5)

        # Hora
        tk.Label(self.frame_entrada, text="Hora (HH:MM):", bg=self.card_color, fg=self.text_color,
                 font=fuente_labels).grid(row=0, column=2, sticky="w", pady=5)
        # Entry con relief="solid" y bd=1 para un borde muy fino y moderno
        self.entrada_hora = tk.Entry(self.frame_entrada, width=10, font=("Helvetica", 10), relief="solid", bd=1)
        self.entrada_hora.grid(row=0, column=3, padx=10, pady=5)

        # Descripción
        tk.Label(self.frame_entrada, text="Descripción:", bg=self.card_color, fg=self.text_color,
                 font=fuente_labels).grid(row=1, column=0, sticky="w", pady=(15, 5))
        self.entrada_descripcion = tk.Entry(self.frame_entrada, width=55, font=("Helvetica", 10), relief="solid", bd=1)
        self.entrada_descripcion.grid(row=1, column=1, columnspan=3, padx=(10, 0), pady=(15, 5), sticky="w")

        # --- COMPONENTES DEL FRAME DE BOTONES ---
        fuente_botones = ("Helvetica", 10, "bold")

        # Botones sin bordes 3D (relief="flat") y con cursor de mano (cursor="hand2")
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", bg=self.btn_add_color, fg="white",
                                     font=fuente_botones, relief="flat", cursor="hand2", padx=15, pady=8,
                                     command=self.agregar_evento)
        self.btn_agregar.pack(side="left", padx=(0, 10))

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Seleccionado", bg=self.btn_del_color,
                                      fg="white", font=fuente_botones, relief="flat", cursor="hand2", padx=15, pady=8,
                                      command=self.eliminar_evento)
        self.btn_eliminar.pack(side="left")

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", bg=self.btn_exit_color, fg="white",
                                   font=fuente_botones, relief="flat", cursor="hand2", padx=20, pady=8,
                                   command=self.salir_app)
        self.btn_salir.pack(side="right")

        # --- COMPONENTES DEL FRAME DE LISTA (TREEVIEW) ---
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings", style="Treeview")

        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        self.tree.column("fecha", width=120, anchor="center")
        self.tree.column("hora", width=100, anchor="center")
        self.tree.column("descripcion", width=450, anchor="w")

        # Scrollbar más limpia usando ttk
        scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # --- MANEJO DE EVENTOS ---
    def agregar_evento(self):
        """Obtiene los datos de los campos de entrada y los añade al TreeView."""
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get()
        descripcion = self.entrada_descripcion.get()

        if not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, completa los campos de Hora y Descripción.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        self.entrada_hora.delete(0, tk.END)
        self.entrada_descripcion.delete(0, tk.END)
        self.entrada_descripcion.focus()

    def eliminar_evento(self):
        """Elimina el evento seleccionado en el TreeView con confirmación previa."""
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showinfo("Información", "Por favor, selecciona un evento para eliminar.")
            return

        respuesta = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de que deseas eliminar este evento?")

        if respuesta:
            for item in seleccion:
                self.tree.delete(item)

    def salir_app(self):
        """Cierra la aplicación de manera segura."""
        self.root.destroy()


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AgendaPersonalApp(ventana_principal)
    ventana_principal.mainloop()
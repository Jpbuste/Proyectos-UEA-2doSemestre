import tkinter as tk
from tkinter import messagebox


class AppTarea:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Master v1.0")
        self.root.geometry("400x500")

        # --- Configuración Estética (Simil-CSS) ---
        self.color_fondo = "#ffffff"  # Blanco puro
        self.color_primario = "#2ecc71"  # Verde esmeralda (Acento)
        self.color_texto = "#2d3436"  # Gris oscuro profesional
        self.color_borde = "#dfe6e9"  # Gris muy claro para bordes

        self.root.configure(bg=self.color_fondo)
        self.fuente_ui = ("Segoe UI", 11)
        self.fuente_negrita = ("Segoe UI", 11, "bold")

        self.crear_widgets()

    def crear_widgets(self):
        # Contenedor con margen (Padding)
        self.main_container = tk.Frame(self.root, bg=self.color_fondo, padx=25, pady=25)
        self.main_container.pack(expand=True, fill="both")

        # Etiqueta de Título
        tk.Label(self.main_container, text="Mis Tareas", font=("Segoe UI", 18, "bold"),
                 bg=self.color_fondo, fg=self.color_texto).pack(pady=(0, 20), anchor="w")

        # Campo de Entrada (Entry) estilizado
        # Usamos highlightthickness para crear un borde sutil moderno
        self.entrada = tk.Entry(self.main_container, font=self.fuente_ui, bd=0,
                                highlightthickness=1, highlightbackground=self.color_borde,
                                highlightcolor=self.color_primario, fg=self.color_texto)
        self.entrada.pack(fill="x", ipady=10, pady=(0, 15))
        self.entrada.bind('<Return>', lambda e: self.agregar_tarea())

        # Frame para botones
        frame_botones = tk.Frame(self.main_container, bg=self.color_fondo)
        frame_botones.pack(fill="x", pady=(0, 20))

        # Botón Agregar
        self.btn_add = tk.Button(frame_botones, text="+ Agregar", command=self.agregar_tarea,
                                 bg=self.color_primario, fg="white", font=self.fuente_negrita,
                                 bd=0, cursor="hand2", activebackground="#27ae60", padx=15)
        self.btn_add.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Botón Limpiar
        self.btn_clear = tk.Button(frame_botones, text="Limpiar", command=self.limpiar_todo,
                                   bg="#f1f2f6", fg=self.color_texto, font=self.fuente_ui,
                                   bd=0, cursor="hand2", activebackground="#dfe4ea", padx=15)
        self.btn_clear.pack(side="left", expand=True, fill="x", padx=(5, 0))

        # Listado (ListBox)
        self.lista = tk.Listbox(self.main_container, font=self.fuente_ui, bd=0,
                                highlightthickness=1, highlightbackground=self.color_borde,
                                fg=self.color_texto, selectbackground="#e8f8f5",
                                selectforeground=self.color_primario, activestyle="none")
        self.lista.pack(expand=True, fill="both")

    # --- Lógica de la Aplicación ---
    def agregar_tarea(self):
        tarea = self.entrada.get().strip()
        if tarea:
            self.lista.insert(tk.END, f"  {tarea}")
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")

    def limpiar_todo(self):
        if self.lista.size() > 0:
            if messagebox.askyesno("Confirmar", "¿Deseas borrar todas las tareas?"):
                self.lista.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AppTarea(root)
    root.mainloop()
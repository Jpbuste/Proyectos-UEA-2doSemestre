import tkinter as tk
from tkinter import ttk, messagebox

class AplicacionTareasModernas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x550")
        # Establecemos un tamaño mínimo para que nada se oculte si achicas la ventana
        self.root.minsize(550, 450)
        self.root.configure(bg="#FAFAFA")

        # --- Sistema de Estilos Modernos (UI) ---
        self.style = ttk.Style()
        self.style.theme_use('clam') 

        self.style.configure("TFrame", background="#FAFAFA")
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        self.style.configure("Add.TButton", background="#4CAF50", foreground="white", borderwidth=0) 
        self.style.configure("Complete.TButton", background="#2196F3", foreground="white", borderwidth=0) 
        self.style.configure("Clear.TButton", background="#FF9800", foreground="white", borderwidth=0) 
        self.style.configure("Delete.TButton", background="#F44336", foreground="white", borderwidth=0) 
        self.style.configure("TEntry", fieldbackground="#FFFFFF", padding=8, font=("Segoe UI", 11), borderwidth=1)
        
        self.style.configure("Treeview", font=("Segoe UI", 11), rowheight=40, borderwidth=0)
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.style.map("Treeview", background=[('selected', '#E3F2FD')], foreground=[('selected', '#000000')])

        # --- Construcción de la Interfaz ---
        
        # 1. Título (Arriba)
        lbl_titulo = tk.Label(self.root, text="✓ Mis Tareas", font=("Segoe UI", 22, "bold"), bg="#FAFAFA", fg="#2C3E50")
        lbl_titulo.pack(side=tk.TOP, pady=(25, 15))

        # 2. Contenedor superior (Arriba)
        frame_input = ttk.Frame(self.root)
        frame_input.pack(side=tk.TOP, pady=10, padx=25, fill=tk.X)

        self.entrada_tarea = ttk.Entry(frame_input, style="TEntry")
        self.entrada_tarea.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 15))
        self.entrada_tarea.bind("<Return>", self.anadir_tarea)

        btn_anadir = ttk.Button(frame_input, text="Añadir Tarea", style="Add.TButton", command=self.anadir_tarea)
        btn_anadir.pack(side=tk.RIGHT)

        # 3. Contenedor inferior (¡LO EMPAQUETAMOS ABAJO ANTES QUE LA LISTA!)
        frame_acciones = ttk.Frame(self.root)
        frame_acciones.pack(side=tk.BOTTOM, pady=20, padx=25, fill=tk.X)

        btn_completar = ttk.Button(frame_acciones, text="Marcar Completada", style="Complete.TButton", command=self.marcar_completada)
        btn_completar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        btn_limpiar = ttk.Button(frame_acciones, text="Limpiar Completadas", style="Clear.TButton", command=self.limpiar_completadas)
        btn_limpiar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))

        btn_eliminar = ttk.Button(frame_acciones, text="Eliminar Tarea", style="Delete.TButton", command=self.eliminar_tarea)
        btn_eliminar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

        # 4. Contenedor central de la Lista (Toma el espacio restante en el medio)
        frame_lista = ttk.Frame(self.root)
        frame_lista.pack(side=tk.TOP, pady=10, padx=25, fill=tk.BOTH, expand=True)

        self.tree_tareas = ttk.Treeview(frame_lista, columns=("tarea",), show="headings", selectmode="browse")
        self.tree_tareas.heading("tarea", text="Descripción de la Tarea", anchor=tk.W)
        self.tree_tareas.column("tarea", anchor=tk.W)
        
        self.tree_tareas.tag_configure('completada', foreground='#9E9E9E', font=("Segoe UI", 11, "overstrike"))
        self.tree_tareas.tag_configure('pendiente', foreground='#212121')

        self.tree_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree_tareas.bind("<Double-1>", self.marcar_completada)

        scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.tree_tareas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_tareas.configure(yscrollcommand=scrollbar.set)

    # --- Lógica y Manejo de Eventos ---

    def anadir_tarea(self, event=None):
        texto = self.entrada_tarea.get().strip()
        if texto:
            self.tree_tareas.insert("", tk.END, values=(texto,), tags=('pendiente',))
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Escribe una tarea antes de añadirla.")

    def marcar_completada(self, event=None):
        seleccion = self.tree_tareas.selection()
        if seleccion:
            item = seleccion[0]
            valores_actuales = self.tree_tareas.item(item, "values")
            texto_tarea = valores_actuales[0]
            
            if not texto_tarea.startswith("✓ "):
                nuevo_texto = f"✓ {texto_tarea}"
                self.tree_tareas.item(item, values=(nuevo_texto,), tags=('completada',))
                self.tree_tareas.selection_remove(item)
        else:
            messagebox.showwarning("Sin selección", "Selecciona una tarea para completarla.")

    def limpiar_completadas(self):
        for item in self.tree_tareas.get_children():
            if 'completada' in self.tree_tareas.item(item, "tags"):
                self.tree_tareas.delete(item)

    def eliminar_tarea(self):
        seleccion = self.tree_tareas.selection()
        if seleccion:
            for item in seleccion:
                self.tree_tareas.delete(item)
        else:
            messagebox.showwarning("Sin selección", "Selecciona una tarea para eliminarla.")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AplicacionTareasModernas(ventana_principal)
    ventana_principal.mainloop()
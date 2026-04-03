import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas - GUI")
        self.root.geometry("400x500")

        # --- Interfaz Gráfica ---
        
        # Campo de entrada
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)
        self.task_entry.focus_set() # Iniciar con el foco en el input

        # Botones de control
        self.btn_add = tk.Button(root, text="Añadir Tarea (Enter)", command=self.add_task, bg="#e1f5fe")
        self.btn_add.pack(pady=5)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(root, font=("Arial", 11), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Botones de acción inferior
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.btn_complete = tk.Button(self.frame_buttons, text="Completar (C)", command=self.complete_task, bg="#c8e6c9")
        self.btn_complete.pack(side=tk.LEFT, padx=5)

        self.btn_delete = tk.Button(self.frame_buttons, text="Eliminar (Del)", command=self.delete_task, bg="#ffcdd2")
        self.btn_delete.pack(side=tk.LEFT, padx=5)

        # --- Atajos de Teclado (Key Bindings) ---
        
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<d>', lambda event: self.delete_task()) # Atajo alternativo 'D'
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    # --- Funciones de Lógica ---

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(index)
            
            # Verificar si ya está completada para no repetir el check
            if "✔" not in task_text:
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"{task_text} ✔")
                # Feedback visual: Cambiar color de fondo del ítem
                self.task_listbox.itemconfig(index, {'fg': 'gray', 'bg': '#f0f0f0'})
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
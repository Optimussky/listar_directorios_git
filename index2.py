from tkinter import messagebox, ttk
import tkinter as tk
from renombrar_archivos import main

code=main()

def show_selection(code):
    
    # Obtener la opción seleccionada.
    extension_replace = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {extension_replace}",
        title="Selección"
    )
    return code(extension_replace)


main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(
    state="readonly",
    values=["","_", "-", "%", "$"]
)
combo.place(x=50, y=50)
combo.current(2)
button = ttk.Button(text="Mostrar selección", command=show_selection)
button.place(x=50, y=100)
main_window.mainloop()
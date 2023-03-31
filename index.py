# index.py

from tkinter import *
from tkinter import ttk


class Alumno:

    def __init__(self,ventana):


        def enter_data(self):
            extension =  self.extension_entry.get()

            print(f"Extensión: {self.extension}")

        self.ventana=ventana
        self.ventana.title("Renombrar archivos")
        marco=LabelFrame(self.ventana, text="Alumno")
        #marco.grid(row=0, column=0,  padx=10 ,pady=20)
        marco.grid(row=0, column=0)
        
        # Nombre
        Label(marco, text="Extensión").grid(row=1,column=0)
        self.extension_entry=Entry(marco).grid(row=1, column=1)
        
        # Select 
        select_title= Label(marco, text="Selección").grid(row=2, column=0)
        self.select_combobox= ttk.Combobox(marco, values=["","_","-","%","$"," "])
        self.select_combobox.current(2)
        self.select_combobox.grid(row=2, column=1)
        
        # Clave
        #Label(marco, text="Clave").grid(row=4,column=0)
        #Entry(marco).grid(row=4, column=1)
        
        # Asignar
        self.boton_asignar=ttk.Button(marco, text="Asignar",command=enter_data).grid(row=5,columnspan=2, sticky=W+E)

        for widget in marco.winfo_children():
            widget.grid_configure(padx=20, pady=20)

    


if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    ventana.mainloop()

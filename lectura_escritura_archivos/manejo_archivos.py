#manejo_archivos.py
from tkinter import filedialog as fd
#from filedialog import askopenfile
import os


def abrir_archivo():
    filetypes = (('text files','*.txt'),('All files','*.*'))
    #location = fd.askopenfilename(filetypes=[('Todos','*.*')])
    location = fd.askopenfilename(initialdir = ".\\", title = "open file",filetypes = (("Archivos de texto", "*.txt"),("Todos los Archivos","*.*")))

    if location:
        location = str(location)
        ruta = ruta = os.path.abspath(location)
    return str(ruta)


def establecer_archivo(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def leer_archivo(archivo):
    contenido = archivo.read()
    return contenido

def escribir_archivo(archivo, texto):
    archivo.write(texto)


archivo = abrir_archivo()
arch = establecer_archivo(archivo,'r+')
#print("\n",leer_archivo(arch),"\n")
texto = input("Introduzca texto: ")
escribir_archivo(arch, texto+'\n')
arch.seek(0)
print("\n",leer_archivo(arch),"\n")

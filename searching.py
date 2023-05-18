#searching.py
#import tkinter as tk
from tkinter import filedialog as fd
import os
from os import system

filetypes = (('text files','*.txt'),('All files','*.*'))
archivo = fd.askopenfilename(initialdir = ".\\", title = "open file", filetypes = (("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*"))) 
#Abrir
print(archivo) #imprime la ruta del archivo en la consola
#archivo = fd.askopenfile(filetypes=filetypes)
file = str(archivo)
#print(file)
"""
Programa que permite buscar una palabra dentro de un archivo.txt
"""

#archivo = "lee.txt"
salida = "result.txt"

busqueda = input("\nIngresa busqueda: ")
lineas_escribir = []
with open(file, 'r') as archivo_lectura:
    numero_linea = 0
    for linea in archivo_lectura:
        numero_linea += 1
        linea = linea.rstrip()
        separado = linea.split()
        if busqueda in separado:
            lineas_escribir.append(str(numero_linea) + " - " + linea)

with open(salida, "w") as archivo_salida:
    for linea in lineas_escribir:
        archivo_salida.write(linea + "\n")
print('\nSe ha generado un nuevo archivo llamado result.txt\n')
listado = os.listdir()
for x in listado:
    print(x)
print('\n')
print('\nContenido del archivo result\n')
here = system(f'cat {salida}')
"""	Extraer u obtener la extensión
	de un archivo en Python usando
	os.path
	
# 	@author ®Alberto Romero™ DDS - CDMX February 2023
"""
from get_list_dir import listar_directorio
import os.path
from pathlib import Path

archivos = listar_directorio()
#print(type(archivos))
#print("")

def listar_extensiones(archivos):
    start = 0
    stop = len(archivos)
    listado = []
    print("\nListar directorio de archivos: {int(start:archivos}")
    for archivo in range(start,stop):
        listado = listado.append(archivos[archivo])
        print(listado)
        
        #nombre, extension = os.path.splitext(listado[archivo])
        #print("El archivo '{}' se llama '{}' y tiene la extensión '{}'".format(
         #   archivo, nombre, extension))

listar_extensiones(archivos)
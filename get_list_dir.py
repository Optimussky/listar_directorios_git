"""	Listar archivos de un directorio
    usando os.listdir()
	
# 	@author ®Alberto Romero™ DDS - CDMX February 2023
"""
import os
from pathlib import Path


def listar_directorio(): 
    directorio = os.listdir()
    return f"Desde listar_directorio",directorio




listin = listar_directorio()
def recorre_archivo_en_directorio(listin):
    #listin = listar_directorio()
    
    print(f"Listin desde recorre_archivo_en_directorio : {listin}\n")

    #print(type(listin))
    #if listin.is_file
    for file_name in listin:
        print(listin)
        if Path(file_name).is_file():
            return f"Archivo - {file_name}"
        else:
            return f"Directorio - {file_name}"

        #print(file_name)
        
recorre_archivo_en_directorio(listin)

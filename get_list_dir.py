"""	Listar archivos de un directorio
    usando os.listdir()
	
# 	@author ®Alberto Romero™ DDS - CDMX February 2023
    Updated at: 03-05-2023
"""
import os
from pathlib import Path


def listar_directorio(): 
    directorio = os.listdir()
    #return f"Desde listar_directorio",directorio
    return directorio




#listin = listar_directorio()
directorio = listar_directorio()
def recorre_archivo_en_directorio(directorio):
    #listin = listar_directorio()
    
    #print(f"Listin desde recorre_archivo_en_directorio : {listin}\n")

    #print(f"Tipo de LISTIN", {type(listin)})
    #if listin.is_file
    file_list = []
    directory_list = []
    for file_name in directorio:
        #print(listin)
        if Path(file_name).is_file():
            file_list.append(file_name)
            #return f"Archivo - {file_name}\n"
        else:
            directory_list.append(file_name)
            #return f"Directorio - {file_name}"
    
    
    print(f"Archivos: ",[n for n in file_list ],"\n")
    print(f"Directorios: ",[n for n in directory_list ],"\n")

        #print(file_name)
        
recorre_archivo_en_directorio(directorio)

"""	Extraer u obtener la extensión
	de un archivo en Python usando
	os.path
	
 	@author ®Alberto Romero™ DDS - CDMX February 2023
"""
import os
from pathlib import Path
#from get_list_dir import listar_directorio
#import os.path
#from pathlib import Path


def listar_directorio():
    """ Función listar_directorio es una función que retorna el listado de archivos
    y directorios en el mismo lugar donde se ejecuta este script
    """
    directorio = os.listdir()
    #return f"Desde listar_directorio",directorio
    return directorio


directorio = listar_directorio()



#def recorre_archivo_en_directorio(directorio):
def listar_extensiones(archivos):
    """
    Funcion listar_extensiones recibe un parámetro, mismo que proviene de una función que retorna una lista de archivos y directorios para
    ser procesados dentro de listar_extensiones
    """
    # declarando variable para usar en contador
    k = 0
    listado = []
    total_array = []
    
    for archivo in archivos:    
        file_list = []
        directory_list = []
               
        if Path(archivo).is_file():
            file_list.append(archivo)
            nombre, extension = os.path.splitext(archivo)
            
            if extension != '':
                total = total_array.append(archivo)
                # Contador incrementado a +1
                k=k+1
                print(f"Archivo [{archivo}] - nombre: [{nombre}] - extension: <{extension}>")
                
            else:
                print(f"Archivo [{archivo}] - nombre: [{nombre}] - SIN extension")
                    
        else:
            directory_list.append(archivo)
            #return f"Directorio - {directory_list}"    
    #print(f"Directorios: ",[n for n in directory_list ],"\n")

    return k
    
total = listar_extensiones(directorio)
print(f"\n\nTotal de archivos con extensión: {total}")        
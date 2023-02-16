
import os
from pathlib import Path


def listar_directorio(): 
    directorio = os.listdir()
    #return f"Desde listar_directorio",directorio
    for file_name in directorio:
        return file_name

files = listar_directorio()
def valida_si_es_archivo(files):
    if Path(files).is_file():
        size_dir = len(listin)
        return file_name

listin = listar_directorio()
size_dir = len(listin)
print(listin)
#print(size_dir)
        
        
    
print(listin)
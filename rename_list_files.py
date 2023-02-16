"""	Renombrar archivos
    en Python usando el módulo
	os
	
# 	@author ®Alberto Romero™ DDS - CDMX February 2023
"""
import os
from get_list_dir import recorre_archivo_en_directorio, listar_directorio

archivos = listar_directorio()
def rename_a(archivos):
    ''' Replace " " by "-" '''
    #self.pdf_list_and_num() # redefine: "self.pdf_list", "self.num_pdf_list"
    for i in archivos:
        
        file_name = i
        #cadena_limpia = " ".join( file_name.split(' ') )
        cadena_limpia = " ".join( file_name.split())
        cadena_limpia = file_name.replace(" ", "_")
        if "_.pdf" in cadena_limpia:
            cadena_limpia = cadena_limpia.replace("_.pdf", ".pdf")
            new_file_name = cadena_limpia
            os.rename(file_name, str(new_file_name))
        else:
            new_file_name = cadena_limpia
            os.rename(file_name, str(new_file_name))

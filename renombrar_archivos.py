# renombrar_archivos.py
import re
import os

from tkinter import filedialog

def main(extension_replace):

    folder_selected = filedialog.askdirectory()

    if not folder_selected:
        exit()

    path = f"{str(folder_selected)}"
    os.chdir(path)


    #extension_replace = input("Introduce extensión de archivos para trabajar: [.txt, .jpg...]>> ")
    file_list = filter((lambda x: str(extension_replace) in x), os.listdir(path))
    string_replace = input("Introduce el tipo de caracter: '-' '_' '%'>> ")
    cont = 1
    for i in file_list:
        try:
            x = i.replace(extension_replace,"")
            x = " ".join( x.split())
            x = re.sub(r"\s+$","",x+extension_replace)
            x = x.replace(" ",string_replace)
            
            print("New File: "+x)

            current_file = i
            new_file = x
            new_file = os.rename(current_file,new_file)
            

            cont = cont + 1

        except:
            print(">>> That file didn't work for some reason.")

                
    new_file_list = filter((lambda x: str(extension_replace) in x), os.listdir(path))
    print("")

    for i in new_file_list:
        print(i)

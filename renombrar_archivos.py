# renombrar_archivos.py
# pip install mutagen
import re
from mutagen.easyid3 import EasyID3
import os

from tkinter import filedialog

folder_selected = filedialog.askdirectory()

if not folder_selected:
    exit()

path = f"{str(folder_selected)}"
os.chdir(path)


extension_replace = input("Introduce extensión de archivos para trabajar: [.txt, .jpg...]>> ")
file_list = filter((lambda x: str(extension_replace) in x), os.listdir(path))
string_replace = input("Introduce el tipo de caracter: '-' '_' '%'>> ")
cont = 1
for i in file_list:
    #print("Current File: "+i)
    try:
        x = i.replace(extension_replace,"")
        x = " ".join( x.split())
        x = re.sub(r"\s+$","",x+extension_replace)
        x = x.replace(" ",string_replace)
        
        
        
        print("New File: "+x)
        #y = x.replace(".txt","").strip('').replace(" ",f"{string_replace}")
        #print(y[0],"Y en 0")
        #print(y[1],"Y en 1")
        
        current_file = i
        new_file = x
        new_file = os.rename(current_file,new_file)
        #print(f"\n {new_file}")

        cont = cont + 1

    except:
        print(">>> That file didn't work for some reason.")

                      
new_file_list = filter((lambda x: str(extension_replace) in x), os.listdir(path))
print("")
for i in new_file_list:
    print(i)
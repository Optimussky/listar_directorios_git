#<iframe src ="<? echo "http://fatiga.ssc.cdmx.gob.mx/pid/anuncios.php?idS=$idS";?>;" width="100%" height="200" frameborder=0 scrolling="auto">

from tkinter import *
from tkinter import filedialog
import re
import os, sys
import time
from os import listdir
from os.path import isfile, join
from pathlib import Path


class LeeTexto:

    def PreguntarRuta():
        root = Tk()
        root.title("Seleccionar Carpeta")
        root.geometry("800x400+10+10")
        root.fileName = filedialog.askdirectory()
        time.sleep(0.5)
        root.destroy()
        return root.fileName


    def Cambiar_nombre_archivos(lista2):

        for i in lista2:
            nombre_original = i
            if ".py" not in i:
                nombre_recortado = LeeTexto.Recortar_Cadena(i)
                ruta1 = "fileName" + nombre_original
                ruta2 = "fileName" + nombre_recortado

            os.rename(ruta1,ruta2)

    def Recortar_Cadena(nombre):

        tamano_id = 15 # El tamaño de derecha a izquierda
        total = len(nombre) # Total de la cadena (Archivo nombre)
        i = total - tamano_id # Restamo 5 al total
        nuevo_nombre = nombre[i:total]
        return nuevo_nombre

    def Leer_directorio():
        mi_ruta = LeeTexto.PreguntarRuta()
        solo_archivos = [
                f for f in listdir(mi_ruta)
                if isfile(join(mi_ruta,f))]
        print(solo_archivos)
        lista_nueva = []
        for archivo in solo_archivos:
            lista_nueva.append(archivo)
        LeeTexto.Cambiar_nombre_archivos(lista_nueva)


ejecutar=LeeTexto
ejecutar.Leer_directorio()

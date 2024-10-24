from libro import Libro
from lector import Lector
from typing import List

def cargar_libros(archivo):
    libros = []
    try:
        with open(archivo,"r") as file:
            for linea in file:
                codigo,titulo,autor,disponibilidad = linea.split("-")
                # lista_cadenas = linea.split("-")
                # codigo = lista_cadenas[0]
                # titulo = lista_cadenas[1]
                # autor = lista_cadenas[2]
                # disponibilidad = lista_cadenas[3]
                libros.append(Libro(titulo,autor,True))
    except FileNotFoundError:
        print("El archivo de libros no existe, se comenzará con una lista vacía de libros.")
    return libros

def guardar_libros(libros_actualizados:List[Libro],archivo):
    try:
        with open(archivo,"w") as file:
            lineas = []
            for libro in libros_actualizados:
                lineas.append(f"{libro.codigo}-{libro.titulo}-{libro.autor}-{libro.disponible}\n")
            file.writelines(lineas)
    except Exception as error:
        print("Error inesperado:",error)

def cargar_lectores(archivo):
    lectores = []
    try:
        with open(archivo,"r") as file:
            for linea in file:
                id_usuario,nombre = linea.strip("\n").split("-")
                lectores.append(Lector(nombre))
    except FileNotFoundError:
        print("El archivo de lectores no existe, se comenzará con una lista vacía de lectores.")
    return lectores

def guardar_lectores(lectores_actualizados:List[Lector],archivo):
    try:
        with open(archivo,"w") as file:
            lineas = []
            for lector in lectores_actualizados:
                lineas.append(f"{lector.id_usuario}-{lector.nombre}\n")
            file.writelines(lineas)
    except Exception as error:
        print("Error inesperado:",error)

def registrar_log(mensaje):
    try:
        with open("log.txt","a") as log:
            log.write(mensaje+"\n")
    except FileNotFoundError:
        with open("log.txt","w") as log:
            log.write(mensaje)



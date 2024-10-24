from libro import Libro
from lector import Lector
from administrador import Administrador
from excepciones import *
from prestamo import Prestamo
from utils import *
from typing import List
import os 
from datetime import datetime


def menu_lectores(lectores:List[Lector]):
    while True:
        print("----------Gestión de lectores----------")
        print("________________________________________")
        print("1. Agregar lector")
        print("2. Listar lectores")
        print("3. Eliminar lector")
        print("4. Volver al menú principal")
        print("\n")
        opcion = input("Selecciona una opción (1, 2, 3 o 4)")
        os.system("clear")

        if opcion == "1":
            nombre = input("Ingrese el nombre del lector: ")
            nuevo_lector = Lector(nombre)
            lectores.append(nuevo_lector)
            print(f"Se agregó el lector {nuevo_lector}")
        elif opcion == "2":
            print("Estos son todos los lectores registrados: \n")
            for lector in lectores:
                print(lector)
        elif opcion == "3":
            try:
                id_ = int(input("Ingresa el número de id del lector que deseas eliminar: "))
                lector_seleccionado = None
                for lector in lectores:
                    if lector.id_usuario == id_:
                        lector_seleccionado = lector
                lectores.remove(lector_seleccionado)
            except ValueError:
                print("El id ingresado no es válido o no se encuentra en la lista de lectores.")
            else:
                print("El lector fue eliminado correctamente.")
        elif opcion == "4":
            print("Volviendo al menú principal")
            break
        else:
            print("Opción no válida, intente nuevamente.")
        
        input("Presiona ENTER para continuar...")
        os.system("clear")

def menu_libros(libros:List[Libro],admin:Administrador):
    while True:
        print("-----------Gestión de libros-----------")
        print("________________________________________")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Eliminar libro")
        print("4. Volver al menú principal")
        print("\n")
        opcion = input("Selecciona una opción (1, 2, 3 o 4)")
        os.system("clear")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            nuevo_libro = Libro(titulo,autor,True)
            admin.agregar_libro(nuevo_libro,libros)
            print(f"Se agregó el libro {nuevo_libro}")
        elif opcion == "2":
            print("Estos son todos los libros registrados: \n")
            for libro in libros:
                print(f"Código: {libro.codigo}, Título:",libro)
        elif opcion == "3":
            try:
                codigo = int(input("Ingresa el número de id del libro que deseas eliminar: "))
                libro_seleccionado = None
                for libro in libros:
                    if libro.codigo == codigo:
                        libro_seleccionado = libro
                admin.eliminar_libro(libro_seleccionado,libros)
            except ValueError:
                print("El código ingresado no es válido.")
            except LibroNoEncontradoError as error:
                print(error)
            else:
                print("El libro fue eliminado correctamente.")
        elif opcion == "4":
            print("Volviendo al menú principal")
            break
        else:
            print("Opción no válida, intente nuevamente.")
        
        input("Presiona ENTER para continuar...")
        os.system("clear")

def menu_prestamos(prestamos:List[Prestamo],libros:List[Libro],lectores:List[Lector]):
    while True:
        print("----------Gestión de Préstamos----------")
        print("________________________________________")
        print("1. Registrar préstamo")
        print("2. Listar préstamos")
        print("3. Hacer devolución")
        print("4. Volver al menú principal")
        print("\n")
        opcion = input("Selecciona una opción (1, 2, 3 o 4)")
        os.system("clear")

        if opcion == "1":
            try:
                cod_libro = int(input("Ingrese el código del libro solicitado: "))
                libro = None
                for l in libros:
                    if l.codigo == cod_libro:
                        libro = l
                if libro == None:
                    raise LibroNoEncontradoError("El código de libro ingresado no está registrado. Revise el listado de libros e intente nuevamente.")
                
                id_usuario = int(input("Ingrese el id del usuario que solicita el libro: "))
                lector = None
                for l in lectores:
                    if l.id_usuario == id_usuario:
                        lector = l
                if lector == None:
                    raise LectorNoEncontrado("El id del lector ingresado no está registrado. Revise el listado de lectores e intente nuevamente.")

                dia = int(input("Ingrese el número del día de devolución: "))
                mes = int(input("Ingrese el número del mes de devolución: "))
                anio = int(input("Ingrese el año de devolución: "))
                fecha_devolucion = datetime(year=anio,month=mes,day=dia)

                prestamo = Prestamo(lector,libro,fecha_devolucion)
            except ValueError:
                print("El tipo de dato ingresado no es válido. Intente nuevamente.")
                del prestamo
            except LibroNoEncontradoError as error:
                print(error)
                del prestamo
            except LectorNoEncontrado as error:
                print(error)
                del prestamo
            except LibroNoDisponibleError as error:
                print(error)
                del prestamo
            except Exception as error:
                print(error)
                del prestamo
            else:
                prestamos.append(prestamo)
        elif opcion == "2":
            print("Listado de préstamos registrados\n")
            for prestamo in prestamos:
                print(f"Libro #{prestamo.libro.codigo}, Título:",prestamo)
        elif opcion == "3":
            try:
                cod_devolucion = int(input("Ingrese el código del libro que se quiere devolver: "))
                devolucion = None
                for prestamo in prestamos:
                    if prestamo.libro.codigo == cod_devolucion:
                        devolucion = prestamo
                if devolucion == None:
                    raise PrestamoNoRegistrado("El libro ingresado no ha sido prestado.")
            except ValueError:
                print("El código ingresado no es válido.")
            except PrestamoNoRegistrado as error:
                print(error)
            except LibroNoDisponibleError as error:
                print(error)
            else:
                devolucion.eliminar_prestamo()
                prestamos.remove(devolucion)
        elif opcion == "4":
            print("Volviendo al menú principal")
            break
        else:
            print("Opción no válida, intente nuevamente.")
        
        input("Presiona ENTER para continuar...")
        os.system("clear")


def menu_principal():
    admin = Administrador("admin")
    libros = cargar_libros("libros.txt")
    lectores = cargar_lectores("lectores.txt")
    prestamos = []
    while True:
        print("----Sistema de gestión de Biblioteca----")
        print("________________________________________")
        print("1. Gestionar lectores")
        print("2. Gestionar libros")
        print("3. Gestionar préstamos")
        print("4. Guardar cambios y salir.")
        print("\n")
        opcion = input("Selecciona una opción (1, 2, 3 o 4)")
        os.system("clear")

        if opcion == "1":
            menu_lectores(lectores)
        elif opcion == "2":
            menu_libros(libros,admin)
        elif opcion == "3":
            menu_prestamos(prestamos,libros,lectores)
        elif opcion == "4":
            guardar_libros(libros,"libros.txt")
            guardar_lectores(lectores,"lectores.txt")
            os.system("clear")
            print("Los cambios se guardaron y el programa finalizó correctamente.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
        input("Presiona ENTER para continuar...")
        os.system("clear")


menu_principal()
from dataclasses import dataclass, field
from usuario import Usuario
from libro import Libro
from typing import List
from excepciones import LibroNoEncontradoError


@dataclass
class Administrador(Usuario):
    
    @staticmethod
    def agregar_libro(libro:Libro, libros:List[Libro]):
        libros.append(libro)
        print(f"Se ha agregado el libro {libro} correctamente.")
        return libros
    
    @staticmethod
    def eliminar_libro(libro:Libro,libros:List[Libro]):
        if libro not in libros:
            raise LibroNoEncontradoError(f"El libro {libro} no está registrado.")
        libros.remove(libro)
        print(f"El libro {libro} se ha eliminado correctamente.")
        return libros

    @classmethod
    def contar_libros_disponibles(cls, libros:List[Libro]):
        return sum(1 for libro in libros if libro.disponible)
    
    
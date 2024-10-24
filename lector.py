from dataclasses import dataclass, field
from usuario import Usuario
from libro import Libro
from typing import List
from excepciones import LibroNoDisponibleError

@dataclass
class Lector(Usuario):
    __libros_prestados:list = field(default_factory=list, init=False)
    

    @property
    def libros_prestados(self):
        return self.__libros_prestados
    
    @libros_prestados.setter
    def libros_prestados(self,lista_libros:List[Libro]):
        self.__libros_prestados = lista_libros
    
    def tomar_prestado(self, libro:Libro):
        if libro in self.libros_prestados:
            raise LibroNoDisponibleError(f"El lector ya tiene el libro {libro}.")
        self.libros_prestados.append(libro)
    
    def devolver_libro(self,libro:Libro):
        if libro not in self.libros_prestados:
            raise LibroNoDisponibleError(f"El libro {libro} no lo tiene el lector")
        self.libros_prestados.remove(libro)
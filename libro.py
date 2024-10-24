from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Libro:
    __titulo:str
    __autor:str
    __disponible:bool
    __cod_libro:int = field(default=-1,init=False)
    __contador_libros: ClassVar = field(default=0,repr=False)
    __codigos_usados: ClassVar = field(default=set(),repr=False)

    def __post_init__(self):
        cod_asignable = 0
        while not Libro.validar_codigo(cod_asignable):
            cod_asignable += 1
        self.__cod_libro = cod_asignable
        Libro.__codigos_usados.add(self.__cod_libro)
        Libro.__contador_libros += 1
    
    @property
    def codigo(self):
        return self.__cod_libro
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor

    @property
    def disponible(self):
        return self.__disponible
    
    @disponible.setter
    def disponible(self, estado:bool):
        self.__disponible = estado
    
    @classmethod
    def contar_libros(cls):
        return cls.__contador_libros
    
    @staticmethod
    def validar_codigo(codigo):
        return codigo not in Libro.__codigos_usados and type(codigo) == int
    
    def __str__(self):
        return f"'{self.__titulo}' de {self.__autor}"

# libro1 = Libro("titulo","autor",1,True)
# libro2 = Libro("titulo","autor",1,True)

# print(Libro.contar_libros())
# libro3 = Libro("titulo","autor",1,True)
# print(Libro.contar_libros())
from dataclasses import dataclass, field
from typing import ClassVar
from excepciones import *

@dataclass
class Usuario:
    __nombre:str
    __id_usuario:int = field(default=-1,init=False)
    __contador_usuarios: ClassVar = field(default=0,repr=False)
    __ids_usados: ClassVar = field(default=set(),repr=False)

    def __post_init__(self):
        id_asignable = 0
        while not Usuario.validar_id(id_asignable):
            id_asignable += 1
        self.__id_usuario = id_asignable
        Usuario.__ids_usados.add(self.__id_usuario)
        Usuario.__contador_usuarios += 1

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def id_usuario(self):
        return self.__id_usuario
    
    @id_usuario.setter
    def id_usuario(self,nuevo_id):
        try:
            if Usuario.validar_id(nuevo_id):
                Usuario.__ids_usados.remove(self.__id_usuario)
                Usuario.__ids_usados.add(nuevo_id)
                self.__id_usuario = nuevo_id
            else:
                raise IdInvalidoError("Se está intentando modificar el id por uno no válido.")
        except KeyError as k_err:
            print(f"ALERTA: Se está intentando eliminar un id no registrado (ID #{self.__id_usuario})")
            print("ID's registrados correctamente:\n")
            Usuario.listar_ids()
        except IdInvalidoError as id_err:
            print(f"ERROR: {id_err.msje}")
            print("Los siguientes números de ID ya están en uso:")
            Usuario.listar_ids()
            correccion = int(input("Ingrese un número entero que no esté en la lista de arriba:\n"))
            self.id_usuario = correccion

    @classmethod
    def contar_usuarios(cls):
        return cls.__contador_usuarios
    
    @staticmethod
    def validar_id(id_):
        return id_ not in Usuario.__ids_usados and type(id_) == int
    
    @classmethod
    def listar_ids(cls):
        print("---------")
        for id in cls.__ids_usados:
            print(f"ID #{id}")
        print("---------")
    
    def __str__(self):
        return f"#{self.id_usuario} {self.nombre}"

    
user = Usuario("Diego")

print(repr(user))
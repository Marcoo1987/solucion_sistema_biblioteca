from dataclasses import dataclass, field
from lector import Lector
from libro import Libro
from datetime import datetime
from excepciones import LibroNoDisponibleError
from utils import registrar_log


@dataclass
class Prestamo:
    __lector:Lector
    __libro:Libro
    __fecha_prestamo:datetime = field(default=datetime.now(),init=False)
    __fecha_devolucion:datetime = field(default=None)

    def __post_init__(self):
        if not self.validar_fecha_devolucion():
            raise Exception("La fecha de devolución ingresada debe ser posterior a la fecha de registro del préstamo")
        self.registrar_prestamo()

    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo
    
    @fecha_prestamo.setter
    def fecha_prestamo(self,nueva_fecha:datetime):
        self.__fecha_prestamo = nueva_fecha
    
    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion
    
    @fecha_devolucion.setter
    def fecha_devolucion(self,nueva_fecha:datetime):
        if nueva_fecha < self.fecha_prestamo:
            raise ValueError("La fecha de devolución no puede ser anterior a la fecha de préstamo.")
        self.__fecha_devolucion = nueva_fecha

    @property
    def libro(self):
        return self.__libro

    def validar_fecha_devolucion(self):
        return self.fecha_devolucion > self.fecha_prestamo

    def registrar_prestamo(self):
        if not self.__libro.disponible:
            raise LibroNoDisponibleError(f"El libro {self.__libro} no está disponible")
        self.__lector.tomar_prestado(self.__libro)
        self.__libro.disponible = False
        registrar_log(f"{datetime.now()} --- {self.__lector} tomó el libro {self.__libro}")
        print(f"{self.__lector} se llevó el libro {self.__libro} con éxito.")

    def eliminar_prestamo(self):
        self.__lector.devolver_libro(self.__libro)
        self.__libro.disponible = True
        registrar_log(f"{datetime.now()} --- {self.__lector} devolvió el libro {self.__libro}")
        print(f"{self.__lector} devolvió el libro {self.__libro} exitosamente.")
    
    def __str__(self):
        return f"{self.__libro} fue prestado a {self.__lector} desde el {self.fecha_prestamo.date()} hasta el {self.fecha_devolucion.date()}."



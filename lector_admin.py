from dataclasses import dataclass
from lector import Lector
from administrador import Administrador


@dataclass
class LectorAdministrador(Lector,Administrador):
    pass

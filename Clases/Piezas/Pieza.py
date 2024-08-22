from abc import ABC, abstractmethod

class Pieza(ABC):
    
    def __init__(self, nombre, color, fila, columna):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fila__ = fila
        self.__columna__ = columna

    # Método para ver la fila de la pieza
    @property
    def fila(self):
        return self.__fila__

    # Método para cambiar la fila de la pieza
    @fila.setter
    def fila(self, value):
        self.__fila__ = value

    # Método para ver la columna de la pieza 
    @property
    def columna(self):
        return self.__columna__

    # Método para cambiar la columna de la pieza
    @columna.setter
    def columna(self, value):
        self.__columna__ = value

    # Metodo para verificar si el movimiento de la pieza es valido
    @abstractmethod
    def verificar_movimiento(self, fila, columna):
        pass


class MovimientoRecto(Pieza):
    def __init__(self, nombre, color, fila, columna):
        super().__init__(nombre, color, fila, columna)
    
    def verificar_movimiento(self, fila, columna):
        if self.fila == fila or self.columna == columna:
            return True
        else:
            return False
        
class MovimientoDiagonal(Pieza):
    def __init__(self, nombre, color, fila, columna):
        super().__init__(nombre, color, fila, columna)
    
    def verificar_movimiento(self, fila, columna):
        if abs(self.fila - fila) == abs(self.columna - columna):
            return True
        else:
            return False

class MovimientoPeon(Pieza):    
    def __init__(self, nombre, color, fila, columna):
        super().__init__(nombre, color, fila, columna)
    
    def verificar_movimiento(self, fila, columna):
        if self.fila == fila and abs(self.columna - columna) == 1:
            return True
        else:
            return False
        
class MovimientoCaballo(Pieza):
    def __init__(self, nombre, color, fila, columna):
        super().__init__(nombre, color, fila, columna)
    
    def verificar_movimiento(self, fila, columna):
        if (abs(self.fila - fila) == 2 and abs(self.columna - columna) == 1) or (abs(self.fila - fila) == 1 and abs(self.columna - columna) == 2):
            return True
        else:
            return False
        
class MovimientoRey(Pieza):
    def __init__(self, nombre, color, fila, columna):
        super().__init__(nombre, color, fila, columna)
    
    def verificar_movimiento(self, fila, columna):
        if abs(self.fila - fila) <= 1 and abs(self.columna - columna) <= 1:
            return True
        else:
            return False
from abc import ABC, abstractmethod

class Pieza(ABC):
    
    def __init__(self, nombre, color, fila, columna, movimiento = None):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fila__ = fila
        self.__columna__ = columna
        self.__movimiento__ = movimiento
    
    def __str__(self):
        if self.__color__ == 'blanco':
            return self.pieza_blanca 
        else:
            return self.pieza_negra 

    @property
    def movimiento(self):
        return self.__movimiento__

    @property
    def fila(self):
        return self.__fila__

    @fila.setter
    def fila(self, value):
        self.__fila__ = value

    @property
    def columna(self):
        return self.__columna__

    @columna.setter
    def columna(self, value):
        self.__columna__ = value

    @property
    def color(self):
        return self.__color__
    
    # Metodo para verificar si el movimiento de la pieza es valido
    @abstractmethod
    def verificar_movimiento(self, fila, columna):
        pass

        
class PiezaId(Pieza):
        
    def __init__(self, nombre, color, id, fila, columna, movimiento = None):
        super().__init__(nombre, color, fila, columna, movimiento)
        self.__id__ = id

    def __str__(self):
        if self.__color__ == 'blanco':
            return self.pieza_blanca + str(self.__id__)
        else:
            return self.pieza_negra + str(self.__id__)
            
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

    @property
    def color(self):
        return self.__color__
    
    # Metodo para verificar si el movimiento de la pieza es valido
    @abstractmethod
    def verificar_movimiento(self, fila, columna):
        pass

class Pieza:
    
    def __init__(self, nombre, color, fila, columna):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fila__ = fila
        self.__columna__ = columna

    #Metodo para poder ver la fila de la pieza
    @property
    def fila(self):
        return self.__fila__

    #Metodo para poder ver la columna de la pieza 
    @property
    def columna(self):
        return self.__columna__ 
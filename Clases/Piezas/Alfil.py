from .Pieza import Pieza

class Alfil(Pieza):

    def __init__(self, color, id, fila, columna):
        super().__init__('Torre', color, fila, columna)
        self.__id__ = id


    def __str__(self):  
        if self.__color__ == 'blanco':
            return f'♗{self.__id__}'
        else:
            return f'♝{self.__id__}'
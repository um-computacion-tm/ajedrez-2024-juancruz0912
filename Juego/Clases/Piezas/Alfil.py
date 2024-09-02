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
        
    def verificar_movimiento(self, fila, columna):
        if abs(self.fila - fila) == abs(self.columna - columna):
            self.__movimiento__ = 'Diagonal' 
            return True
        else:
            raise ValueError('El movimiento no es diagonal')


 
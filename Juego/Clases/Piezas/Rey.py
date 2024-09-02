from .Pieza import Pieza 

class Rey(Pieza):

    def __init__(self, color, fila, columna, movimiento = None):
        super().__init__('Rey', color, fila, columna, movimiento)

    def __str__(self):
        if self.__color__ == 'blanco':
            return '♔ '
        else:
            return '♚ '
        
    def verificar_movimiento(self, fila, columna):
        if abs(self.__fila__ - fila) <= 1 and abs(self.__columna__ - columna) <= 1:
            if abs(self.__fila__ - fila) == abs(self.__columna__ - columna):
                self.__movimiento__ = 'Diagonal' 
                return True
            else:  
                self.__movimiento__ = 'Recto' 
                return True
        else:  
            raise ValueError('El movimiento no es valido')
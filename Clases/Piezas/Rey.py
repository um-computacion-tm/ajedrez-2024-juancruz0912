from .Pieza import Pieza 

class Rey(Pieza):

    def __init__(self, color, fila, columna):
        super().__init__('Rey', color, fila, columna)

    def __str__(self):
        if self.__color__ == 'blanco':
            return '♔ '
        else:
            return '♚ '
        
    def verificar_movimiento(self, fila, columna):
        if self.__fila__ == fila and self.__columna__ == columna:
            raise ValueError('EL rey no se puede mover a la misma posición')
        elif abs(self.fila - fila) <= 1 and abs(self.columna - columna) <= 1:
            return 'Recto'
        elif abs(self.__fila__ - fila) == abs(self.__columna__ - columna):
            return 'Diagonal'
        else:  
            raise ValueError('El movimiento no es valido')
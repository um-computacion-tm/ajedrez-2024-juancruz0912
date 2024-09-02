from .Pieza import Pieza
   
class Reina(Pieza):

    def __init__(self, color, fila, columna, movimiento = None):
        super().__init__('Reina', color, fila, columna, movimiento)

    def __str__(self):
        if self.__color__ == 'blanco':
            return '♕ '
        else:
            return '♛ '

    def verificar_movimiento(self, fila, columna):
        if self.fila == fila or self.columna == columna:
            self.__movimiento__ = 'Recto' 
            return True
        elif abs(self.__fila__ - fila) == abs(self.__columna__ - columna):
            self.__movimiento__ = 'Diagonal' 
            return True
        else:  
            raise ValueError('El movimiento no es valido')
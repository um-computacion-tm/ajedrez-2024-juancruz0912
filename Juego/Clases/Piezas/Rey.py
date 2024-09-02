from .Pieza import Pieza 

class Rey(Pieza):

    pieza_blanca = '♔ '
    pieza_negra = '♚ '

    def __init__(self, color, fila, columna, movimiento = None):
        super().__init__('Rey', color, fila, columna, movimiento)

        
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
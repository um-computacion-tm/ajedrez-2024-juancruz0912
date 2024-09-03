from .Pieza import Pieza 

class Rey(Pieza):

    pieza_blanca = '♔ '
    pieza_negra = '♚ '

    def __init__(self, color, fila, columna, movimiento = None):
        super().__init__('Rey', color, fila, columna, movimiento)

        
    def verificar_movimiento(self, fila, columna):
        if self.diagonal_un_lugar(fila, columna):
            self.__movimiento__ = 'Diagonal' 
            return True
        elif self.recto_un_lugar(fila, columna):  
            self.__movimiento__ = 'Recto' 
            return True
        else:  
            raise ValueError('El movimiento no es valido')
        
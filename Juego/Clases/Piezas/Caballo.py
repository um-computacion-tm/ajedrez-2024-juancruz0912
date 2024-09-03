from .Pieza import PiezaId

class Caballo(PiezaId):

    pieza_blanca = '♘'
    pieza_negra = '♞'

    def __init__(self, color, id, fila, columna, movimiento = None):
        super().__init__('Caballo', color, id, fila, columna, movimiento)

    def verificar_movimiento(self, fila, columna):
        if self.caballo(fila, columna):
            self.__movimiento__ = 'Caballo' 
            return True
        else:
            raise ValueError('Movimiento no valido')
        
    def caballo(self, fila, columna):
        if (abs(self.fila - fila) == 2 and abs(self.columna - columna) == 1) or (abs(self.fila - fila) == 1 and abs(self.columna - columna) == 2):
            return True
        else:
            return False
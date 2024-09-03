from .Pieza import PiezaId 

class Torre(PiezaId):

    pieza_blanca = '♖'
    pieza_negra = '♜'

    def __init__(self, color, id, fila, columna, movimiento = None):
        super().__init__('Peon', color, id, fila, columna, movimiento)

    
    def verificar_movimiento(self, fila, columna):
        if self.recto(fila, columna):
            self.__movimiento__ = 'Recto'
            return True
        else:
            raise ValueError('Movimiento no valido')
        
    def recto(self, fila, columna):
        if self.__fila__ == fila or self.__columna__ == columna:
            return True
        else:
            return False
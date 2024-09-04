from .Pieza import PiezaId

class Alfil(PiezaId):

    pieza_blanca = '♗'
    pieza_negra = '♝'

    def __init__(self, color, id, fila, columna, movimiento = None):
        super().__init__('Alfil', color, id, fila, columna, movimiento)

        
    def verificar_movimiento(self, fila, columna):
        if self.es_movimiento_diagonal(fila, columna):
            self.__movimiento__ = 'Diagonal' 
            return True
        else:
            raise ValueError('El movimiento no es diagonal')


 
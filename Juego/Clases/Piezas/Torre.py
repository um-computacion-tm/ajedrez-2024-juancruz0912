from .Pieza import PiezaId 

class Torre(PiezaId):

    pieza_blanca = '♖'
    pieza_negra = '♜'

    def __init__(self, color, id, fila, columna, movimiento = None):
        super().__init__('Torre', color, id, fila, columna, movimiento)

    
    def verificar_movimiento(self, fila, columna):
        if self.es_movimiento_recto(fila, columna):
            self.__movimiento__ = 'Recto'
            return True
        else:
            raise ValueError('Movimiento no valido')
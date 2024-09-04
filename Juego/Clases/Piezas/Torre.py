from .Pieza import PiezaId 

class Torre(PiezaId):

    pieza_blanca = '♖'
    pieza_negra = '♜'

    def __init__(self, color, **kwargs):
        self.__columna__ = 1 if kwargs['id'] == 1 else 8 
        super().__init__('Torre', color, id=kwargs['id'], columna = self.__columna__)

    
    def verificar_movimiento(self, fila, columna):
        if self.es_movimiento_recto(fila, columna):
            self.__movimiento__ = 'Recto'
            return True
        else:
            raise ValueError('Movimiento no valido')
from .Pieza import PiezaId

class Alfil(PiezaId):

    pieza_blanca = '♗'
    pieza_negra = '♝'


    def __init__(self, color, **kwargs):
        self.__columna__ = 3 if kwargs['id'] == 1 else 6 
        super().__init__('Alfil', color, id=kwargs['id'], columna = self.__columna__)

        
    def verificar_movimiento(self, fila, columna):
        return self.es_movimiento_diagonal(fila, columna, 'Diagonal')
            


 
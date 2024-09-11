from .Pieza import PiezaId

class Alfil(PiezaId):

    pieza_blanca = '♗'
    pieza_negra = '♝'
    c1 = 3
    c2 = 6 

    def __init__(self, color, **kwargs):

        super().__init__('Alfil', color, id=kwargs['id'])


    def verificar_movimiento(self, fila, columna):
        return self.es_movimiento_diagonal(fila, columna, 'Diagonal')
            


 
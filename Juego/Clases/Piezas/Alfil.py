from .Pieza import PiezaId

class Alfil(PiezaId):

    pieza_blanca = '♗'
    pieza_negra = '♝'
    

    def __init__(self, color, **kwargs):
        c1 = 3
        c2 = 6
        super().__init__('Alfil', color, id=kwargs['id'], c1 = c1 , c2 = c2)

        
    def verificar_movimiento(self, fila, columna):
        return self.es_movimiento_diagonal(fila, columna, 'Diagonal')
            


 
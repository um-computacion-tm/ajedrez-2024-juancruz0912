from .pieza import PiezaId

class Alfil(PiezaId):

    pieza_blanca = '♗'
    pieza_negra = '♝'
    c1 = 3
    c2 = 6 

    def __init__(self, color, **kwargs):
        self.configurar_pieza('Alfil', color, id=kwargs['id'], movimiento='Diagonal')

    def movimiento_especifico(self, fila, columna):
        return self.es_movimiento_diagonal(fila, columna, 'Diagonal')
            


 
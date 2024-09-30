from .pieza import PiezaId

class Caballo(PiezaId):

    pieza_blanca = '♘'
    pieza_negra = '♞'
    c1 = 2  
    c2 = 7

    def __init__(self, color, **kwargs):         
        super().__init__('Caballo', color, id=kwargs['id'])


    def movimiento_especifico(self, fila, columna):
        return self.es_movimiento_caballo(fila, columna)

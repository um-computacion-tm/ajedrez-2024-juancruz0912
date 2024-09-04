from .Pieza import PiezaId

class Caballo(PiezaId):

    pieza_blanca = '♘'
    pieza_negra = '♞'


    def __init__(self, color, **kwargs):
        c1 = 2  
        c2 = 7
        super().__init__('Caballo', color, id=kwargs['id'], c1 = c1, c2 = c2)


    def verificar_movimiento(self, fila, columna):
        return self.movimiento_caballo(fila, columna)
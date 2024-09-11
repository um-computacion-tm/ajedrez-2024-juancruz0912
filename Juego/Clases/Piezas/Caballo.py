from .Pieza import PiezaId

class Caballo(PiezaId):

    pieza_blanca = '♘'
    pieza_negra = '♞'
    c1 = 2  
    c2 = 7

    def __init__(self, color, **kwargs):        
        super().__init__('Caballo', color, id=kwargs['id'])


    def verificar_movimiento(self, fila, columna):
        return self.movimiento_caballo(fila, columna)
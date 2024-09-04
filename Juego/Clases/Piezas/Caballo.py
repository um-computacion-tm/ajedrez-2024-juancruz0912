from .Pieza import PiezaId

class Caballo(PiezaId):

    pieza_blanca = '♘'
    pieza_negra = '♞'

    def __init__(self, color, id, fila, columna, movimiento = None):
        super().__init__('Caballo', color, id, fila, columna, movimiento)


    def verificar_movimiento(self, fila, columna):
        return self.caballo(fila, columna)
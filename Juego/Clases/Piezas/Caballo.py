from .Pieza import PiezaId

class Caballo(PiezaId):

    pieza_blanca = '♘'
    pieza_negra = '♞'


    def __init__(self, color, **kwargs):
        self.__columna__ = 2 if kwargs['id'] == 1 else 7 
        super().__init__('Caballo', color, id=kwargs['id'], columna = self.__columna__)


    def verificar_movimiento(self, fila, columna):
        return self.movimiento_caballo(fila, columna)
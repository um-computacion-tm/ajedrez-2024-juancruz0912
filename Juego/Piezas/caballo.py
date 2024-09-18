from .pieza import PiezaId

class Caballo(PiezaId):

    pieza_blanca = '♘'
    pieza_negra = '♞'
    c1 = 2  
    c2 = 7

    def __init__(self, color, **kwargs):         
        super().__init__('Caballo', color, id=kwargs['id'])
        self.__movimiento__ = 'Caballo'


    def movimiento_especifico(self, fila, columna):
        if (abs(self.fila - fila) == 2 and abs(self.columna - columna) == 1) or (abs(self.fila - fila) == 1 and abs(self.columna - columna) == 2):
            return True
        else:
            return False
from .Pieza import PiezaReyes
   
class Reina(PiezaReyes):

    pieza_blanca = '♕ '
    pieza_negra = '♛ '
    c1 = 4

    def __init__(self, color):
        super().__init__('Reina', color)


    def movimiento_especifico(self, fila, columna):
        return self.reyes(fila, columna)
from .Pieza import PiezaReyes
   
class Reina(PiezaReyes):

    pieza_blanca = '♕ '
    pieza_negra = '♛ '
    columna = 4

    def __init__(self, color):
        super().__init__('Reina', color, columna = self.columna)


    def verificar_movimiento(self, fila, columna):
        return self.reyes(fila, columna)
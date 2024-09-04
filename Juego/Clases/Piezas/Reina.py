from .Pieza import PiezaReyes
   
class Reina(PiezaReyes):

    pieza_blanca = '♕ '
    pieza_negra = '♛ '

    def __init__(self, color):
        self.__columna__ = 4
        super().__init__('Reina', color, columna = self.__columna__)


    def verificar_movimiento(self, fila, columna):
        return self.reyes(fila, columna)
from .Pieza import Pieza
   
class Reina(Pieza):

    pieza_blanca = '♕ '
    pieza_negra = '♛ '

    def __init__(self, color, fila, columna, movimiento = None):
        super().__init__('Reina', color, fila, columna, movimiento)


    def verificar_movimiento(self, fila, columna):
        self.reina(fila, columna)
        

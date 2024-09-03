from .Pieza import Pieza 

class Rey(Pieza):

    pieza_blanca = '♔ '
    pieza_negra = '♚ '

    def __init__(self, color, fila, columna, movimiento = None):
        super().__init__('Rey', color, fila, columna, movimiento)

        
    def verificar_movimiento(self, fila, columna):
        self.rey(fila, columna)
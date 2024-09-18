from .Pieza import PiezaReyes

class Rey(PiezaReyes):

    pieza_blanca = '♔ '
    pieza_negra = '♚ '
    c1 = 5

    def __init__(self, color):
        super().__init__('Rey', color)

        
    def movimiento_especifico(self, fila, columna):
        if self.un_paso(fila, columna):
            return self.reyes(fila, columna)
        else:  
            return False
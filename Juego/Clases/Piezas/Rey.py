from .Pieza import PiezaReyes

class Rey(PiezaReyes):

    pieza_blanca = '♔ '
    pieza_negra = '♚ '

    def __init__(self, color):
        self.__columna__ = 5
        super().__init__('Rey', color, columna = self.__columna__)

        
    def verificar_movimiento(self, fila, columna):
        if self.un_paso(fila, columna):
            return self.reyes(fila, columna)
        else:  
            return False
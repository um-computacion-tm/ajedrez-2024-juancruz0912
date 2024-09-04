from .Pieza import Pieza 

class Rey(Pieza):

    pieza_blanca = '♔ '
    pieza_negra = '♚ '

    def __init__(self, color):
        self.__columna__ = 5 
        self.__fila__ = 1 if color == 'negro' else 8
        super().__init__('Rey', color, columna = self.__columna__, fila = self.__fila__)

        
    def verificar_movimiento(self, fila, columna):
        if self.un_paso(fila, columna):
            return self.reyes(fila, columna)
        else:  
            return False
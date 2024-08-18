from .Pieza import Pieza 

class Rey(Pieza):

    def __init__(self, color, fila, columna):
        super().__init__('Rey', color, fila, columna)

    def __str__(self):
        if self.__color__ == 'blanco':
            return '♔ '
        else:
            return '♚ '
from .Pieza import Pieza
   
class Reina(Pieza):

    def __init__(self, color, columna, fila):
        super().__init__('Reina', color, fila, columna)

    def __str__(self):
        if self.__color__ == 'blanco':
            return '♛'
        else:
            return '♕'

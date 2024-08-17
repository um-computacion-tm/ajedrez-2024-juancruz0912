from .Pieza import Pieza

class Torre(Pieza):

    def __init__(self, color, id, columna, fila):
        super().__init__('Torre', color, id, fila, columna)

    def __str__(self):
        if self.__id__ == 1: 
            if self.__color__ == 'blanco':
                return '♜1'
            else:
                return '♖1'
        else:
            if self.__color__ == 'blanco':
                return '♜2'
            else:
                return '♖2'
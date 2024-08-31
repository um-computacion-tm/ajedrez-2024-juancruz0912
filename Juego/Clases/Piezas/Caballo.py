from .Pieza import Pieza

class Caballo(Pieza):

    def __init__(self, color, id, fila, columna):
        super().__init__('Caballo', color, fila, columna)
        self.__id__ = id


    def __str__(self):
        if self.__color__ == 'blanco':
            return f'♘{self.__id__}'
        else:
            return f'♞{self.__id__}'

    def verificar_movimiento(self, fila, columna):
        if (abs(self.fila - fila) == 2 and abs(self.columna - columna) == 1) or (abs(self.fila - fila) == 1 and abs(self.columna - columna) == 2):
            return 'Caballo'
        else:
            raise ValueError('Movimiento no valido')
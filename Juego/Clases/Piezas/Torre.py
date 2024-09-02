from .Pieza import Pieza

class Torre(Pieza):

    def __init__(self, color, id, fila, columna, movimiento = None):
        super().__init__('Torre', color, fila, columna, movimiento)
        self.__id__ = id

    def __str__(self):
       if self.__color__ == 'blanco':
           return f'♖{self.__id__}'
       else:
           return f'♜{self.__id__}'

    def verificar_movimiento(self, fila, columna):
        if self.__fila__ == fila or self.__columna__ == columna:
            self.__movimiento__ = 'Recto'
            return True
        else:
            raise ValueError('Movimiento no valido')
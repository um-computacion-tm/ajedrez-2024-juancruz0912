from .Pieza import Pieza 

class Peon(Pieza):

    def __init__(self, color, id, fila, columna):
        super().__init__('Peon', color, fila, columna)
        self.__id__ = id


    def __str__(self):
        if self.__color__ == 'blanco':
            return f'♙{self.__id__}'
        else:
            return f'♟{self.__id__}'
        
    def verificar_movimiento(self, fila, columna):
        if self.__color__ == 'blanco':
            if self.fila == 7:
                if fila == 6 or fila == 5:
                    return 'Recto'
                else:
                    raise ValueError('El peon se puede mover una o dos casillas hacia adelante')
            elif fila == self.fila - 1:
                return 'Recto'
        
        elif self.__color__ == 'negro':
            if self.fila == 2:
                if fila == 3 or fila == 4:
                    return 'Recto'
                else:
                    raise ValueError('El peon se puede mover una o dos casillas hacia adelante')
            elif fila == self.fila + 1:
                return 'Recto'
        else:
            raise ValueError('Movimiento invalido')
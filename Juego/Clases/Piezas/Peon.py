from .Pieza import PiezaId 

class Peon(PiezaId):

    pieza_blanca = '♙'
    pieza_negra = '♟'

    def __init__(self, color, id, fila, columna, movimiento = None):
        super().__init__('Peon', color, id, fila, columna, movimiento)

    def verificar_movimiento(self, fila, columna):
        if self.columna == columna:
            if self.__color__ == 'blanco':
                if self.fila == 7:
                    if fila == 6 or fila == 5:
                        self.__movimiento__ = 'Recto' 
                        return True
                    else:
                        raise ValueError('El peon se puede mover una o dos casillas hacia adelante')
                elif fila == self.fila - 1:
                    self.__movimiento__ = 'Recto' 
                    return True
                else:
                    raise ValueError('El peon se puede mover una casilla hacia adelante')
            elif self.__color__ == 'negro':
                if self.fila == 2:
                    if fila == 3 or fila == 4:
                        self.__movimiento__ = 'Recto' 
                        return True
                    else:
                        raise ValueError('El peon se puede mover una o dos casillas hacia adelante')
                elif fila == self.fila + 1:
                    self.__movimiento__ = 'Recto' 
                    return True
                else:
                    raise ValueError('El peon se puede mover una casilla hacia adelante')
        elif abs(self.__fila__ - fila) == 1 and abs(self.__columna__ - columna) == 1:
            self.__movimiento__ = 'Comer' 
            return True
        else:
            raise ValueError('El peon solo se puede mover en línea recta')
        

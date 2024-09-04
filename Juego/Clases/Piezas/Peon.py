from .Pieza import PiezaPeon

class Peon(PiezaPeon):

    pieza_blanca = '♙'
    pieza_negra = '♟'

    def __init__(self, color, **kwargs):
        self.__primer_movimiento__ = False
        self.__columna__ = kwargs['id']  
        super().__init__('Peon', color, id=kwargs['id'],  columna = self.__columna__)


    def verificar_movimiento(self, fila, columna):
        if self.columna == columna:
            paso = -1 if self.color == 'blanco' else 1
            if self.__primer_movimiento__ == False:
                self.primer_movimiento(fila, paso)
            elif fila == self.fila + paso:
                self.__movimiento__ = 'Recto' 
                return True
            else:
                raise ValueError('El peon se puede mover una casilla hacia adelante')
        elif self.un_paso(fila, columna):
            if self.es_movimiento_diagonal(fila, columna):
                self.__movimiento__ = 'Comer' 
                return True
        else:
            raise ValueError('El peon solo se puede mover en línea recta')
        
    def primer_movimiento(self, fila, paso):
        if fila == self.fila + paso or fila == self.fila + 2 * paso:
            self.__movimiento__ = 'Recto'
            self.__primer_movimiento__ = True
            return True
        else:
            raise ValueError('El peon se puede mover una o dos casillas hacia adelante')

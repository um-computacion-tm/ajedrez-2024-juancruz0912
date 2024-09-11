from .Pieza import PiezaPeon

class Peon(PiezaPeon):

    pieza_blanca = '♙'
    pieza_negra = '♟'

    def __init__(self, color, **kwargs):
        self.__primer_movimiento__ = False
        self.c1 = self.c2 = kwargs['id']
        super().__init__('Peon', color, id=kwargs['id'])


    def verificar_movimiento(self, fila, columna):
        if self.columna == columna:
            paso = -1 if self.color == 'blanco' else 1
            if self.__primer_movimiento__ == False:
                return self.primer_movimiento(fila, paso)
            elif fila == self.fila + paso:
                self.__movimiento__ = 'Recto' 
                return True
            else:
                return False
        elif self.un_paso(fila, columna):
            return self.es_movimiento_diagonal(fila, columna, 'Comer')
        else:
            return False
        
    def primer_movimiento(self, fila, paso):
        if fila == self.fila + paso or fila == self.fila + 2 * paso:
            self.__movimiento__ = 'Recto'
            self.__primer_movimiento__ = True
            return True
        else:
            return False

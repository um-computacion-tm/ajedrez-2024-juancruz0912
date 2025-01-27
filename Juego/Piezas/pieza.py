from abc import ABC, abstractmethod

class Pieza(ABC):
    
    def __init__(self, nombre, color, columna, fila):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fila__ = fila
        self.__columna__ = columna
    
    def __str__(self):
        if self.__color__ == 'blanco':
            return self.pieza_blanca 
        else:
            return self.pieza_negra 


    @property
    def fila(self):
        return self.__fila__

    @fila.setter
    def fila(self, value):
        self.__fila__ = value

    @property
    def columna(self):
        return self.__columna__

    @columna.setter
    def columna(self, value):
        self.__columna__ = value

    @property
    def color(self):
        return self.__color__
    
    # Metodo para verificar si el movimiento de la pieza es valido
    @abstractmethod
    def movimiento_especifico(self, fila, columna): # pragma: no cover
        pass

    def verificar_movimiento(self, fila, columna):
        return self.movimiento_especifico(fila, columna)

    def es_movimiento_recto(self, fila, columna):
        if self.__fila__ == fila or self.__columna__ == columna:
            return True
        else:
            return False
        

    def es_movimiento_diagonal(self, fila, columna, mensaje):
        if abs(self.__fila__ - fila) == abs(self.__columna__ - columna):
            return True
        else:
            return False

    def es_movimiento_caballo(self, fila, columna):
        return (abs(self.fila - fila) == 2 and abs(self.columna - columna) == 1) or (abs(self.fila - fila) == 1 and abs(self.columna - columna) == 2)

    def reyes(self, fila, columna):
        if self.es_movimiento_recto(fila, columna):
            return True
        elif self.es_movimiento_diagonal(fila, columna, False):
            return True
        else:  
            return False

    def un_paso(self, fila, columna):
        return abs(self.__fila__ - fila) <= 1 and abs(self.__columna__ - columna) <= 1
        
class PiezaId(Pieza):
        
    def __init__(self, nombre, color, id):
        self.__id__ = id
        self.__fila__ = 1 if color == 'negro' else 8  
        self.__columna__ = self.c1 if id == 1 else self.c2 
        super().__init__(nombre, color, columna = self.__columna__, fila = self.__fila__)

    def __str__(self):
        return f"{self.pieza_blanca}{self.__id__}" if self.__color__ == 'blanco' else f"{self.pieza_negra}{self.__id__}"
    

# clase especial para la reina y el rey
class PiezaReyes(Pieza):
    def __init__(self, nombre, color):
        self.__columna__ = self.c1
        self.__fila__ = 1 if color == 'negro' else 8 
        super().__init__(nombre=nombre, color=color, columna= self.__columna__, fila= self.__fila__)


# clase especial para los peones, donde todos tiene misma fila
class PiezaPeon(PiezaId):
    
    def __init__(self, nombre, color, id, **kargs):
        super().__init__(nombre, color, id, **kargs)
        self.__fila__ = 2 if color == 'negro' else 7  
        self.__columna__ = id
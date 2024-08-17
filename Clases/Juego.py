from Piezas import Torre
from Piezas import Alfil  
from Piezas import Caballo
from Piezas import Reina
from Piezas import Rey

class Tablero:
    def __init__(self):
        self.__tablero__ = [[" " for i in range(9)] for i in range(9)]
        self.__tablero__[0] = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
        self.__tablero__[1][1] = Torre("negro", 1, 1, 1)
        self.__tablero__[1][1] = Alfil("negro", 1, 1, 2)
        self.__tablero__[1][1] = Caballo("negro", 1, 1, 3)
        self.__tablero__[1][1] = Reina("negro", 1, 4)
        self.__tablero__[1][1] = Rey("negro", 1, 5)
        self.__tablero__[1][1] = Caballo("negro", 1, 1, 6)
        self.__tablero__[1][1] = Alfil("negro", 1, 1, 7)
        self.__tablero__[1][1] = Torre("negro", 1, 1, 8)
        self.__piezas__ = {'TN1': Torre('negro', 1, 1, 1), }
        for i in range(1, 9):
            self.__tablero__[i][0] = str(i)
        
    
    #Metodo para mostrar el tablero en la terminal
    def imprimir_tablero(self):
        print("   " + " | ".join(self.__tablero__[0][1:]) + " |")
        for fila in self.__tablero__[1:]:
            fila_str = [str(celda) if celda is not None else "   " for celda in fila]
            print(" | ".join(fila_str) + " |")
            linea = '--+' + '---+' * (len(fila) - 1)
            print(linea)


    #Metodo para ver el contenido de una celda en espedifico, lo inputs son el numero de fila y de columna
    def ver_celda(self, fila, columna):
        if self.__tablero__[fila][columna] == ' ':
            mensaje = 'vacio'
        else:   
            mensaje = self.__tablero__[fila][columna]
        
        print(f'en la cela {fila},{columna} se encuentra : {mensaje}')
        return mensaje


    def mover_pieza(self, x, y, pieza):
        pieza = self.__piezas__[pieza]    
        self.__tablero__[x][y] = self.__tablero__[pieza.__fila__][pieza.__columna__]
        self.__tablero__[pieza.__fila__][pieza.__columna__] = ''


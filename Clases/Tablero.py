from Piezas.Torre import Torre
from Piezas.Alfil import Alfil  
from Piezas.Caballo import Caballo
from Piezas.Reina import Reina
from Piezas.Rey import Rey
from Piezas.Peon import Peon

class Tablero:
    
    def __init__(self):
        self.__tablero__ = [['  ' for i in range(9)] for i in range(9)]
        self.__tablero__[0] = ["   ", " A ", "B ", "C ", "D ", "E ", "F ", "G ", "H "]
        self.__piezas__ = {}
        self.crear_piezas()
        self.colocar_piezas()

    #Metodo para crear las piezas y asignarles la posicion inicial
    def crear_piezas(self):
        self.__piezas__ = {
            'T1 negro': Torre('negro', 1, 1, 1), 
            'CN1': Caballo('negro', 1, 1, 2),
            'AN1': Alfil('negro', 1, 1, 3), 
            'RN': Rey('negro', 1, 4), 
            'DN': Reina('negro', 1, 5), 
            'AN2': Alfil('negro', 2, 1, 6), 
            'CN2': Caballo('negro', 2, 1, 7),
            'TN2': Torre('negro', 2, 1, 8),
            'T1 blanco': Torre('blanco', 2, 8, 1), 
            'CB1': Caballo('blanco', 1, 8, 2),
            'AB1': Alfil('blanco', 1, 8, 3), 
            'RB': Rey('blanco', 8, 4), 
            'DB': Reina('blanco', 8, 5), 
            'AB2': Alfil('blanco', 2, 8, 6), 
            'CB2': Caballo('blanco', 2, 8, 7),
            'TB2': Torre('blanco', 2, 8, 8)
        }
        for i in range(1, 9):
            self.__piezas__[f'PN{i}'] = Peon('negro', i, 2, i)
            self.__piezas__[f'PB{i}'] = Peon('blanco', i, 7, i)

    #Metodo para colocar cada pieza con su posicion correspondiente en el tablero
    def colocar_piezas(self):
        for pieza in self.__piezas__.values():
            fila = pieza.fila
            columna = pieza.columna
            self.__tablero__[fila][columna] = pieza

        for i in range(1, 9):
            self.__tablero__[i][0] = str(9-i)
        
    
    #Metodo para mostrar el tablero en la terminal
    def imprimir_tablero(self):
        print("   " + " | ".join(self.__tablero__[0][1:]) + " |")
        for fila in self.__tablero__[1:]:
            fila_str = [str(celda) if celda is not None else "   " for celda in fila]
            print(" | ".join(fila_str) + " |")
            linea = '--+' + '----+' * (len(fila) - 1)
            print(linea)


    #Metodo para ver el contenido de una celda en espedifico, lo inputs son el numero de fila y de columna
    def ver_celda(self, fila, columna):
        if self.__tablero__[fila][columna] == '  ':
            mensaje = 'vacio'
        else:   
            mensaje = self.__tablero__[fila][columna]
        
        print(f'en la cela {fila},{columna} se encuentra : {mensaje}')
        return mensaje

    # Metodo para mover una pieza en el tablero, donde le paso los parametros de que ficha quiero mover y a que posicion
    def mover_pieza(self, x, y, pieza):
        pieza = self.__piezas__[pieza]    
        self.__tablero__[x][y] = self.__tablero__[pieza.__fila__][pieza.__columna__]
        self.__tablero__[pieza.__fila__][pieza.__columna__] = '   '

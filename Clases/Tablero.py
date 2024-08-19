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
            'TN1': Torre('negro', 1, 1, 1), 
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

    def movimiento_recto_valido(self, x_destino, y_destino, pieza):
        if pieza.fila == x_destino:  # Movimiento horizontal
            paso = 1 if pieza.columna < y_destino else -1
            for columna in range(pieza.columna + paso, y_destino, paso):
                if self.__tablero__[pieza.fila][pieza.columna] != '  ':  # Ocupada
                    raise ValueError(f'La casilla {pieza.fila},{pieza.columna} esta ocupada')
            raise ValueError('El movimiento debe ser en horizontal')
        elif pieza.columna == y_destino:  # Movimiento vertical
            paso = 1 if pieza.fila < x_destino else -1
            for fila in range(pieza.fila + paso, x_destino, paso):
                if self.__tablero__[fila][pieza.columna] != '  ':  # Ocupada
                    raise ValueError(f'La casilla {pieza.fila},{pieza.columna} esta ocupada')
        raise ValueError('El movimiento debe ser en vertical o horizontal')
    
    def movimiento_diagonal_valido(self, x_destino, y_destino, pieza):
        if abs(pieza.fila - x_destino) == abs(pieza.columna - y_destino):  # Movimiento diagonal
            fila_paso = 1 if x_destino > pieza.fila else -1
            columna_paso = 1 if y_destino > pieza.columna else -1
            fila_actual, columna_actual = pieza.fila + fila_paso, pieza.columna + columna_paso
            while fila_actual != x_destino and columna_actual != y_destino:
                if self.__tablero__[fila_actual][columna_actual] != '  ':  # Ocupada
                    raise ValueError(f'La casilla {fila_actual},{columna_actual} esta ocupada')
                fila_actual += fila_paso
                columna_actual += columna_paso
            return True
        raise ValueError('El movimiento debe ser en diagonal')

    #Metodo para mover una pieza, donde se ingresan las variables x(fila), y(columna) y pieza(pieza a mover, Ej: 'TN1')
    def mover_pieza(self, x, y, pieza):
        pieza = self.__piezas__[pieza]
        
        if pieza.verificar_movimiento(x, y) and self.movimiento_recto_valido(x, y, pieza):
            raise ValueError('Movimiento invalido')
        else:
            self.__tablero__[pieza.fila][pieza.columna] = '  '
            pieza.fila = x
            pieza.columna = y    
            self.__tablero__[x][y] = pieza
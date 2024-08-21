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
                'Torre 1 negro': Torre('negro', 1, 1, 1), 
                'Caballo 1 negro': Caballo('negro', 1, 1, 2),
                'Alfil 1 negro': Alfil('negro', 1, 1, 3), 
                'Rey negro': Rey('negro', 1, 4), 
                'Reina negro': Reina('negro', 1, 5), 
                'Alfil 2 negro': Alfil('negro', 2, 1, 6), 
                'Caballo 2 negro': Caballo('negro', 2, 1, 7),
                'Torre 2 negro': Torre('negro', 2, 1, 8),
                'Torre 1 blanco': Torre('blanco', 2, 8, 1), 
                'Caballo 1 blanco': Caballo('blanco', 1, 8, 2),
                'Alfil 1 blanco': Alfil('blanco', 1, 8, 3), 
                'Rey blanco': Rey('blanco', 8, 4), 
                'Reina blanco': Reina('blanco', 8, 5), 
                'Alfil 2 blanco': Alfil('blanco', 2, 8, 6), 
                'Caballo 2 blanco': Caballo('blanco', 2, 8, 7),
                'Torre 2 blanco': Torre('blanco', 2, 8, 8)
        }
        for i in range(1, 9):
            self.__piezas__[f'Peon {i} negro'] = Peon('negro', i, 2, i)
            self.__piezas__[f'Peon {i} blanco'] = Peon('blanco', i, 7, i)
        

    #Metodo para mostrar el tablero
    def __str__(self):
        filas = []

        encabezado = "  |" + " | ".join(self.__tablero__[0][1:]) + " |"
        filas.append(encabezado)
        linea = "--+" + "----+" * 8
        filas.append(linea)

        for i, fila in enumerate(reversed(self.__tablero__[1:]), 1):
            fila_numero = 9 - i  
            fila_str = [f" {str(celda):<3}" for celda in fila[1:]] 
            filas.append(f"{fila_numero} |" + "|".join(fila_str) + "|")
            if fila_numero > 1:
                linea = "--+" + "----+" * 8  
                filas.append(linea)

        linea = "--+" + "----+" * 8
        filas.append(linea)

        return "\n".join(filas)
    
    #Metodo para colocar cada pieza con su posicion correspondiente en el tablero
    def colocar_piezas(self):
        for pieza in self.__piezas__.values():
            fila = pieza.fila
            columna = pieza.columna
            self.__tablero__[fila][columna] = pieza

        for i in range(1, 9):
            self.__tablero__[i][0] = str(9-i)


    # Metodo que verifica si hay alguna pieza en el medio de la trayectoria (Movimientos rectos)
    def movimiento_recto_valido(self, x, y, pieza):
        if pieza.fila == x:  # Movimiento horizontal
            paso = 1 if pieza.columna < y else -1
            for columna in range(pieza.columna + paso, y, paso):
                if self.__tablero__[pieza.fila][columna] != '  ':  # Ocupada
                    raise ValueError(f'La casilla {pieza.fila},{pieza.columna} esta ocupada')
            return True
        
        elif pieza.columna == y:  # Movimiento vertical
            paso = 1 if pieza.fila < x else -1
            for fila in range(pieza.fila + paso, x, paso):
                if self.__tablero__[fila][pieza.columna] != '  ':  # Ocupada
                    raise ValueError(f'La casilla {pieza.fila},{pieza.columna} esta ocupada')
            return True
        raise ValueError('El movimiento debe ser en vertical o horizontal')
    
    # Metodo que verifica si hay alguna pieza en el medio de la trayectoria (Movimientos diagonales)
    def movimiento_diagonal_valido(self, x, y, pieza):    
        fila_paso = 1 if x > pieza.fila else -1
        columna_paso = 1 if y > pieza.columna else -1
        
        fila_actual, columna_actual = pieza.fila + fila_paso, pieza.columna + columna_paso
        while fila_actual != x and columna_actual != y:
            if self.__tablero__[fila_actual][columna_actual] != '  ':  # Ocupada
                raise ValueError(f'La casilla {fila_actual},{columna_actual} esta ocupada')
            fila_actual += fila_paso
            columna_actual += columna_paso
        return True
    
    # Metodo en el cual se mueve la pieza
    def mover_pieza_valida(self, x, y, pieza):
        self.__tablero__[x][y] = self.__tablero__[pieza.__fila__][pieza.__columna__]
        self.__tablero__[pieza.__fila__][pieza.__columna__] = '   '
        pieza.fila = x 
        pieza.columna = y
    
    #Metodo para mover una pieza, donde se ingresan las variables x(fila), y(columna) y pieza(pieza a mover, Ej: 'TN1')
    def mover_pieza_tablero(self, x, y, pieza, turno):
        pieza = self.__piezas__[pieza + ' ' + turno]
        if pieza.verificar_movimiento(x, y) == 'Recto':
            if self.movimiento_recto_valido(x, y, pieza):
                self.mover_pieza_valida(x, y, pieza)
        
        elif pieza.verificar_movimiento(x, y) == 'Diagonal':
            if self.movimiento_diagonal_valido(x, y, pieza):
                self.mover_pieza_valida(x, y, pieza)

        elif pieza.verificar_movimiento(x, y) == 'Caballo':
            self.mover_pieza_valida(x, y, pieza)


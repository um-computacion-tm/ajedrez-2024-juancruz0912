from .Piezas.Torre import Torre
from .Piezas.Alfil import Alfil  
from .Piezas.Caballo import Caballo
from .Piezas.Reina import Reina
from .Piezas.Rey import Rey
from .Piezas.Peon import Peon

class Tablero:
    
    def __init__(self):
        self.__tablero__ = [['  ' for i in range(9)] for i in range(9)]
        self.__piezas__ = {}
        self.__fila1__ = {
            'A': 1,
            'B': 2,  
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8 }
        self.crear_piezas()
        self.colocar_piezas()
        self.primer_fila()

    #Metodo para la primer fila
    def primer_fila(self):
        for letra, numero in self.__fila1__.items():
            self.__tablero__[0][numero] = f' {letra} ' 


    #Metodo para crear las piezas y asignarles la posicion inicial
    def crear_piezas(self):
        self.__piezas__ = {
                'Torre 1 negro': Torre('negro', id = 1), 
                'Caballo 1 negro': Caballo('negro', id = 1),
                'Alfil 1 negro': Alfil('negro', id = 1), 
                'Rey negro': Rey('negro'), 
                'Reina negro': Reina('negro'), 
                'Alfil 2 negro': Alfil('negro', id = 2), 
                'Caballo 2 negro': Caballo('negro', id = 2),
                'Torre 2 negro': Torre('negro', id = 2),
                'Torre 1 blanco': Torre('blanco', id = 1), 
                'Caballo 1 blanco': Caballo('blanco', id = 1),
                'Alfil 1 blanco': Alfil('blanco', id = 1), 
                'Rey blanco': Rey('blanco'), 
                'Reina blanco': Reina('blanco'), 
                'Alfil 2 blanco': Alfil('blanco', id = 2), 
                'Caballo 2 blanco': Caballo('blanco', id = 2),
                'Torre 2 blanco': Torre('blanco', id = 2)
        }
        for i in range(1, 9):
            self.__piezas__[f'Peon {i} negro'] = Peon('negro', id = i) 
            self.__piezas__[f'Peon {i} blanco'] = Peon('blanco', id = i)
        
    def __str__(self):
        filas = []
        encabezado = "\n  |" + "| ".join(self.__tablero__[0][1:]) + " |"
        filas.append(encabezado)
        linea = "--+" + "----+" * 8
        filas.append(linea)

        for i, fila in enumerate(self.__tablero__[1:], 1):
            fila_numero = i  
            fila_str = [f" {str(celda):<3}" for celda in fila[1:]] 
            filas.append(f"{fila_numero} |" + "|".join(fila_str) + "|")
            if fila_numero < 8:
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

    # Metodo para verificar si la pieza ingresada por el usuario existe
    def pieza_existente(self, pieza):
        return pieza in self.__piezas__
    
    #Metodo para verificar si quedan piezas de un color, para ver si el juego se termina o sigue
    def quedan_piezas(self):
        contador_blanco = 0
        contador_negro = 0
        for pieza in self.__piezas__.values():
            if pieza.color == 'blanco':
                contador_blanco += 1 
            else:
                contador_negro += 1
        if contador_blanco == 0: 
            return 'Blanco'
        elif contador_negro == 0:
            return 'Negro'
        else:
            return None
              

    #Metodo para mover una pieza, donde se ingresan las variables x(fila), y(columna) y pieza(pieza a mover, Ej: 'TN1')
    def mover_pieza_tablero(self, x, y, pieza):
        if not (1 <= x <= 8):
            raise ValueError (f'La fila {x} no existe')
        if y not in self.__fila1__:
            raise ValueError(f'La columna {y} no existe')
        y = self.__fila1__[y]
        pieza = self.__piezas__[pieza]
        self.verificar_movimiento(x, y, pieza)  
        
    def que_movimiento(self, x, y, pieza):
        if pieza.verificar_movimiento(x, y):
            movimiento = pieza.movimiento
            if self.mismo_lugar(x, y, pieza):
                if movimiento == 'Recto':
                     return self.movimiento_recto_valido(x, y, pieza)
                elif movimiento == 'Diagonal':
                    return self.movimiento_diagonal_valido(x, y, pieza)
                elif movimiento == 'Caballo':
                    if self.tablero[x][y] == '  ':
                       return True
                    elif self.tablero[x][y].color != pieza.color:
                        return 'Comer'
                    else:
                        return False
                elif movimiento == 'Comer':
                    return self.movimiento_peon_comer(x, y, pieza)
        else:
            return False       

    def verificar_movimiento(self, x, y, pieza):
        mover = self.que_movimiento(x, y, pieza)
        if mover == 'Comer':
            self.comer_pieza(x, y, pieza)
        elif mover == True:
            self.mover_pieza_valida(x, y, pieza)
        else:
            raise ValueError('Movimiento no valido')
        

    # Metodo para verificar si la pieza se movio al mismo lugar
    def mismo_lugar(self, x, y, pieza):
        if pieza.fila == x and pieza.columna == y:
            return False
        else:
            return True

    def movimiento_peon_comer(self, x, y, pieza):
        if self.__tablero__[x][y] != '  ':
            if self.__tablero__[x][y].color != pieza.color:
                return 'Comer'
        else:
            return False

    # Metodo que verifica si hay alguna pieza en el medio de la trayectoria (Movimientos rectos)
    def movimiento_recto_valido(self, x, y, pieza):
        if pieza.fila == x:  # Movimiento horizontal
           return self.movimiento_horizontal(y, pieza)
        elif pieza.columna == y:  # Movimiento vertical
            return self.movimiento_vertical(x, pieza)
        else:
            return False
    
    # Metodo para verificar si hay alguna pieza en el medio de la trayectoria (Movimientos horizontales)
    def movimiento_horizontal(self, y, pieza):
        paso = 1 if pieza.columna < y else -1
        for columna in range(pieza.columna + paso, y, paso):
            if self.__tablero__[pieza.fila][columna] != '  ':  # Ocupada
                return False
        if self.__tablero__[pieza.fila][y] != '  ':
            if self.__tablero__[pieza.fila][y].color != pieza.color:
                return 'Comer'
            else:
                return False
        return True
    
    # Metodo para verificar si hay alguna pieza en el medio de la trayectoria (Movimientos verticales)
    def movimiento_vertical(self, x, pieza):
        paso = 1 if pieza.fila < x else -1
        for fila in range(pieza.fila + paso, x, paso):
            if self.__tablero__[fila][pieza.columna] != '  ':  # Ocupada
                return False
        if self.__tablero__[x][pieza.columna] != '  ':
            if self.__tablero__[x][pieza.columna].color != pieza.color:
                return 'Comer'
            else:
                return False
        return True

    # Metodo que verifica si hay alguna pieza en el medio de la trayectoria (Movimientos diagonales)
    def movimiento_diagonal_valido(self, x, y, pieza):    
        fila_paso = 1 if x > pieza.fila else -1
        columna_paso = 1 if y > pieza.columna else -1
        fila_actual, columna_actual = pieza.fila + fila_paso, pieza.columna + columna_paso
        while fila_actual != x + fila_paso and columna_actual != y + fila_paso:
            if self.__tablero__[fila_actual][columna_actual] != '  ':  # Ocupada
                if self.__tablero__[fila_actual][columna_actual].color != pieza.color:
                    return 'Comer'
                else:
                    return False
            fila_actual += fila_paso
            columna_actual += columna_paso
        return True

    # Metodo para comer una pieza
    def comer_pieza(self, x, y, pieza):
        pieza_comida = self.__tablero__[x][y]
        clave_a_eliminar = None
        for clave, obj in self.__piezas__.items():
            if obj == pieza_comida:
                clave_a_eliminar = clave
                break
        if clave_a_eliminar:
            self.__piezas__.pop(clave_a_eliminar)  # Elimina la pieza comida del diccionario
        self.mover_pieza_valida(x, y, pieza)


    
    # Metodo en el cual se mueve la pieza una vez que ya esta verificado que puede hacer el movimiento
    def mover_pieza_valida(self, x, y, pieza):
        self.__tablero__[pieza.fila][pieza.columna] = '  '
        pieza.fila = x 
        pieza.columna = y
        self.__tablero__[x][y] = pieza
        return True    

    
    # Metodo del jaque mate, donde se verifica primero si alguna pieza le hace jaque, y luego se verifica si alguna pieza puede comer a la pieza que hace el jaque
    # y por ultimo si el rey puede moverse a alguna posicion donde no este en jaque
    def jaque_mate_tablero(self, color, x, y ):
        rey = self.__piezas__.get(f'Rey {color}')
        if self.jaque(color):
            if self.verificar_comer_pieza_jaque(x, y, color):
                self.metodo_jaque_mate(rey, color)
        else:
            return False
        
    
    #Metodo para el jaque, donde se pasa el color del rey que se quiere verificar, 
    # luego de que el jugador blanco mueva, se verifica si el rey negro esta en jaque
    def jaque(self, color):
        rey = self.__piezas__[f'Rey {color}']
        for pieza in self.__piezas__.values():
            if pieza.color != color: #Piezas del otro color del rey
                if self.que_movimiento(rey.fila, rey.columna, pieza) == 'Comer': #Si alguna pieza puede llegar al rey
                    return True
        return False
        
    def metodo_jaque_mate(self, rey, color):
        movimientos_rey = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        return self.verificar_jaque(movimientos_rey, rey, color )
        
    def verificar_jaque(self, movimientos_rey, rey, color):
        jaque_mate = 0
        for dx, dy in movimientos_rey:
            nueva_fila =rey.fila + dx
            nueva_columna = rey.columna + dy
            if 1 <= nueva_fila <= 8 and 1 <= nueva_columna <= 8:  # Verificar si la nueva posición está dentro de los límites del tablero
                nueva_columna = self.convertir_numero_a_letra(nueva_columna)
                if self.verificar_movimiento(nueva_fila, nueva_columna, rey):  # Intentar mover el rey a la nueva posición
                    if self.jaque() == color:  # Si el rey sigue en jaque
                        jaque_mate += 1
                    else:
                        return False
            else:
                 jaque_mate += 1
        if jaque_mate == 8:
            return True
    
    
    def verificar_comer_pieza_jaque(self, x, y, color):
        for pieza in self.piezas.values():
            if pieza.color == color: # verificar si alguna pieza del color del rey puede comer a la pieza que hace jaque
                if self.que_movimiento(x, y, pieza) == 'Comer':
                    return False
        else:
            return True

    # Metodo utilizado en el jaque para convertir el numero de la columna a la letra correspondiente
    def convertir_numero_a_letra(self, numero):
        columnas = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
        return columnas[numero]


    @property
    def tablero(self):
        return self.__tablero__

    @property
    def piezas(self):
        return self.__piezas__
    
    @piezas.setter
    def piezas(self, valor):
        self.__piezas__ = valor


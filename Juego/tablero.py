from Juego.Piezas.torre import Torre
from Juego.Piezas.alfil import Alfil  
from Juego.Piezas.caballo import Caballo
from Juego.Piezas.reina import Reina
from Juego.Piezas.rey import Rey
from Juego.Piezas.peon import Peon

class Tablero:
    
    def __init__(self):
        self.__tablero__ = [['  ' for i in range(9)] for i in range(9)]
        self.__piezas__ = {}
        
        colores = ['negro', 'blanco'] #Inicializar todas las piezas
        for color in colores:
            for i in range(1, 3):
                self.__piezas__[f'Torre {i} {color}'] = Torre(color, id=i)
                self.__piezas__[f'Caballo {i} {color}'] = Caballo(color, id=i)
                self.__piezas__[f'Alfil {i} {color}'] = Alfil(color, id=i)
            self.__piezas__[f'Rey {color}'] = Rey(color)
            self.__piezas__[f'Reina {color}'] = Reina(color)
            for i in range(1, 9):
                self.__piezas__[f'Peon {i} {color}'] = Peon(color, id=i)

            self.__fila1__ = {
            'A': 1,
            'B': 2,  
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8 }
        
        for letra, numero in self.__fila1__.items(): # Se coloca las letras en la parte superior del tablero
            self.__tablero__[0][numero] = f' {letra} ' 

        self.colocar_piezas()

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
              

    #Metodo para mover una pieza, donde se ingresan las variables x(fila), y(columna) y pieza(pieza a mover, Ej: 'Torre')
    def mover_pieza_tablero(self, x, y, pieza):
        if not (1 <= x <= 8):
            raise ValueError (f'La fila {x} no existe')
        if y not in self.__fila1__:
            raise ValueError(f'La columna {y} no existe')
        y = self.__fila1__[y]
        pieza = self.__piezas__[pieza]
        return self.ver_movimiento(x, y, pieza)  # Una vez obtenidos los valores, se verifica si es correcto el movimiento
        
    # Metodo que valida los movimientos
    def validar_movimiento(self, x, y, pieza):
        if pieza.verificar_movimiento(x, y): # Se verifica el movimiento de la propia pieza
            movimiento = pieza.movimiento
            if self.mismo_lugar(x, y, pieza): # Se verifica que no se muevan al mismo lugar
                return movimiento
        raise ValueError('Movimiento no valido')
    
    def ver_movimiento(self, x, y, pieza):
        movimiento = self.validar_movimiento(x, y, pieza)
        if movimiento == 'Recto' or movimiento == 'Diagonal':
            return self.movimiento_tablero_valido(x, y, pieza)
        elif movimiento == 'Caballo':
            return self.movimiento_caballo(x, y, pieza)
        elif movimiento == 'Comer':
            return self.movimiento_peon_comer(x, y, pieza)
    

    # Metodo para verificar si la pieza se movio al mismo lugar
    def mismo_lugar(self, x, y, pieza):
        if pieza.fila == x and pieza.columna == y:
            raise ValueError('La pieza no puede moverse a la misma posicion')
        else:
            return True

    # Metodo que verifica el movimiento del peon al comer
    def movimiento_peon_comer(self, x, y, pieza):
        if self.__tablero__[x][y] != '  ':
            if self.__tablero__[x][y].color != pieza.color:
                return self.comer_pieza(x, y, pieza)
        else:
            raise ValueError(f'El peon solo se mueve en diagonal para comer')
        

    # Metodo que verifica si hay alguna pieza en el medio de la trayectoria (Movimientos rectos y diagonales)
    def movimiento_tablero_valido(self, x, y, pieza):    
        fila_paso = self.definir_paso(pieza.fila, x)
        columna_paso = self.definir_paso(pieza.columna, y)
        fila_actual, columna_actual = pieza.fila + fila_paso, pieza.columna + columna_paso
        while fila_actual != x or columna_actual != y: # verifica todo el camino
            if self.__tablero__[fila_actual][columna_actual] != '  ':  # Ocupada
                raise ValueError(f'La casilla {fila_actual} {columna_actual} esta ocupada por una pieza')
            fila_actual += fila_paso
            columna_actual += columna_paso
        if self.__tablero__[x][y] != '  ': # Si hay una pieza en la posicion final
            if self.__tablero__[x][y].color != pieza.color and not isinstance(pieza, Peon): #Porque el peon no puede comer de frente
                return self.comer_pieza(x, y, pieza)
            else:
                raise ValueError(f'La casilla {x} {y} esta ocupada por una pieza')
        else:
            return self.mover_pieza_valida(x, y, pieza)   
        
    def definir_paso(self, origen, destino):
        paso = 0
        if origen == destino:
            paso = 0
        elif origen < destino:
            paso = 1
        else:
            paso = -1
        return paso
        
        
    # Metodo para verificar el movimiento del caballo
    def movimiento_caballo(self, x, y, pieza):
        if self.tablero[x][y] == '  ':
            return self.mover_pieza_valida(x, y, pieza)
        elif self.tablero[x][y].color != pieza.color:
            return self.comer_pieza(x, y, pieza)
        else:
            raise ValueError(f'La casilla {x} {y} esta ocupada por una pieza de su mismo color')

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
        return self.mover_pieza_valida(x, y, pieza)


    # Metodo en el cual se mueve la pieza una vez que ya esta verificado que puede hacer el movimiento
    def mover_pieza_valida(self, x, y, pieza):
        self.__tablero__[pieza.fila][pieza.columna] = '  '
        pieza.fila = x 
        pieza.columna = y
        self.__tablero__[x][y] = pieza
        return True    


    @property
    def tablero(self):
        return self.__tablero__

    @property
    def piezas(self):
        return self.__piezas__
    
    @piezas.setter
    def piezas(self, valor):
        self.__piezas__ = valor


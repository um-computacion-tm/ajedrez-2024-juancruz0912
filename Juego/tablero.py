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


    #Metodo para mover una pieza, donde se ingresan las variables x(fila), y(columna) y pieza(pieza a mover, Ej: 'Torre')
    def mover_pieza_tablero(self, x, y, pieza):
        y = self.__fila1__[y]
        pieza = self.__piezas__[pieza]
        if self.validar_movimiento(x, y, pieza): # si la casilla destino esta ocupada
            return self.comer_pieza(x, y, pieza)
        else:
            return False
            

    # Metodo que valida los movimientos
    def validar_movimiento(self, x, y, pieza):
        if pieza.fila != x or pieza.columna != y: # Se verifica que no sea al mismo lugar
            if pieza.verificar_movimiento(x, y): # Se verifica el movimiento de la propia pieza
                if isinstance (pieza, Caballo):
                    return True
                else:
                    return self.movimiento_tablero_valido(x, y, pieza) 
        return False


    # Metodo que verifica si hay alguna pieza en el medio de la trayectoria (Movimientos rectos y diagonales)
    def movimiento_tablero_valido(self, x, y, pieza):
        if self.__tablero__[x][y] != '  ':
            if isinstance(pieza, Peon) and y == pieza.columna: # Siendo un movimiento recto y un peon, no puede comer de frente
                return False    
        fila_paso = self.definir_paso(pieza.fila, x)
        columna_paso = self.definir_paso(pieza.columna, y)
        fila_actual, columna_actual = pieza.fila + fila_paso, pieza.columna + columna_paso
        while fila_actual != x or columna_actual != y: # verifica todo el camino
            if self.__tablero__[fila_actual][columna_actual] != '  ':  # Ocupada
                return False
            fila_actual += fila_paso
            columna_actual += columna_paso
        if self.__tablero__[x][y] == '  ' and isinstance(pieza, Peon) and (abs(x - pieza.fila) == abs(y - pieza.columna)): #Si la casilla esta desocupada, el peon no puede moverse en diagonal 
            return False
        return True
        
        
    def definir_paso(self, origen, destino):
        paso = 0
        if origen == destino:
            paso = 0
        elif origen < destino:
            paso = 1
        else:
            paso = -1
        return paso
        
    # Metodo para comer una pieza
    def comer_pieza(self, x, y, pieza):
        if self.__tablero__[x][y] != '  ':
            if self.__tablero__[x][y].color == pieza.color: # caso donde la casilla esta ocupada
                return False
            else:
                if self.__tablero__[x][y].color != pieza.color: # caso donde la casilla esta ocupada por una pieza del otro equipo
                    pieza_comida = self.__tablero__[x][y]
                    clave_a_eliminar = None
                    for clave, obj in self.__piezas__.items():
                        if obj == pieza_comida:
                            clave_a_eliminar = clave
                            break
                    if clave_a_eliminar:
                        self.__piezas__.pop(clave_a_eliminar)  # Elimina la pieza comida del diccionario
        return self.mover_pieza_valida(x, y, pieza) # caso donde la casilla esta vacia o sea del otro color


    # Metodo en el cual se mueve la pieza una vez que ya esta verificado que puede hacer el movimiento
    def mover_pieza_valida(self, x, y, pieza):
        self.__tablero__[pieza.fila][pieza.columna] = '  '
        pieza.fila = x 
        pieza.columna = y
        self.__tablero__[x][y] = pieza
        return True    

    
    # Metodo del jaque mate, el cual se llama al finalizar el truno y se comprueba si el rey del otro equipo esta en jaque 
    # Primero se verifica primero si alguna pieza le hace jaque
    # Luego se verifica la cantidad de piezas que amenazan al rey, si una se verifica si se puede comer la pieza o tapar el camino 
    # Si hay mas de una pieza que amenaza al rey, si es asi lo unico que puede hacer el rey es moverse a algun lugar seguro
    # Si el rey no puede moverse a ningun lugar seguro, entonces es jaque mate
    def jaque_mate_tablero(self, color):
        rey = self.__piezas__[f'Rey {color}']
        if self.jaque(color, rey.fila, rey.columna): # Si el rey se encuentra en jaque, se verifica si hay jaque mate
            if self.salvar_jaque_mate(rey, color):
                return True
            else:
                return False #En este caso hay jaque
        else:
            return False
        
    
    #Metodo para el jaque, donde se verifica si alguna pieza puede comer al rey
    def jaque(self, color, xr, cr):
        for pieza in self.__piezas__.values():
            if pieza.color != color: 
                if self.validar_movimiento(xr, cr, pieza) == True: #Si alguna pieza puede llegar al rey
                    return True
        return False

    # Metodo en el cual se verifica la cantidad de piezas que amenazan al rey, si pueden ser comidas y si pueden ser bloquedas
    def salvar_jaque_mate(self, rey, color):
        piezas_que_comen_al_rey = []
        for pieza in self.piezas.values(): # se hace una lista con todas las piezas que pueden comer al rey
            if pieza.color != color and self.validar_movimiento(rey.fila, rey.columna, pieza) == True: 
                piezas_que_comen_al_rey.append(pieza)
        if len(piezas_que_comen_al_rey) > 1: # si hay mas de una pieza haciendo jaque al rey ninguna pieza va a poder salvar al rey
            return self.verificar_movimiento_rey_jaque(rey, color) # se verifica si se puede mover el rey
        else:
            return self.verificar_comer_pieza_jaque(piezas_que_comen_al_rey, rey, color) # Caso que hay solo una pieza que amenaza al rey
    
    # Metodo que verifica si las piezas que amenazan al rey pueden ser comidas de alguna forma
    def verificar_comer_pieza_jaque(self, piezas_que_comen_al_rey, rey, color):
        pieza = piezas_que_comen_al_rey[0]
        for pieza2 in self.piezas.values(): # se verifica si de alguna forma se puede comer a la pieza que amenaza al rey
            if pieza2.color == color and self.validar_movimiento(pieza.fila, pieza.columna, pieza2) == True: 
                return False #Si la pieza que ponia en jaque al rey puede ser comida 
        return self.verificar_bloquear_camino_jaque(rey, color, pieza) # Si ninguna pieza puede comer a la pieza que pone en jaque al rey, se verifica si pueden bloquear el camino  

    # Metodo que verifica si puedo bloquear el camino de alguna pieza
    def verificar_bloquear_camino_jaque(self, rey, color, pieza_amenaza):
        if isinstance(pieza_amenaza, (Torre, Alfil, Reina)):
            direccion_x = self.definir_paso( rey.fila, pieza_amenaza.fila)
            direccion_y = self.definir_paso(rey.columna, pieza_amenaza.columna)
            if self.explorar_camino_bloqueo(rey, color, pieza_amenaza, direccion_x, direccion_y):
                return False  # Si alguna pieza aliada puede bloquear la amenaza, no es jaque mate
        return self.verificar_movimiento_rey_jaque(rey, color)  # Ninguna pieza puede bloquear la amenaza

    # Metodo que explora el camino para ver si alguna pieza puede bloquear la amenaza
    def explorar_camino_bloqueo(self, rey, color, pieza_amenaza, direccion_x, direccion_y):
        fila_bloqueo = rey.fila + direccion_x
        columna_bloqueo = rey.columna + direccion_y
        while fila_bloqueo != pieza_amenaza.fila or columna_bloqueo != pieza_amenaza.columna:
            if self.pieza_puede_bloquear(fila_bloqueo, columna_bloqueo, color, rey):
                return True  # Si una pieza aliada puede bloquear la amenaza, no es jaque mate
            fila_bloqueo += direccion_x
            columna_bloqueo += direccion_y
        return False # Una pieza no puede bloquear la amenaza

    # Ver si alguna pieza puede bloquear el camino
    def pieza_puede_bloquear(self, fila, columna, color, rey):
        for pieza_aliada in self.__piezas__.values():
            if pieza_aliada.color == color and pieza_aliada != rey and self.validar_movimiento(fila, columna, pieza_aliada) == True:
                return True
        return False


    # Metodo que verifica si el rey puede moverse a algun lugar donde no este en jaque
    def verificar_movimiento_rey_jaque(self, rey, color):
        movimientos_rey = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dx, dy in movimientos_rey:
            nueva_fila = rey.fila + dx
            nueva_columna = rey.columna + dy
            if self.verificar_movimiento_rey(nueva_fila, nueva_columna, rey):  # Verifica si el rey se puede mover a otro lado
                self.__tablero__[nueva_fila][nueva_columna] = rey
                if not self.jaque(color, nueva_fila, nueva_columna):  # Verifica si el rey sigue en jaque
                    self.__tablero__[nueva_fila][nueva_columna] = '  ' 
                    return False  # Si el rey puede moverse a un lugar seguro, no hay jaque mate
                self.__tablero__[nueva_fila][nueva_columna] = '  '  # Restaurar el tablero si sigue en jaque
        return True  # Si no hay ningún lugar seguro, es jaque mate

    # Metodo que verifica si el rey se puede mover a otro lado
    def verificar_movimiento_rey(self, x, y, rey):
        if 1 <= x <= 8 and 1 <= y <= 8:
            if self.__tablero__[x][y] == '  ':
                return True
            elif self.__tablero__[x][y].color != rey.color:
                return True
        return False
    
2
    @property
    def piezas(self):
        return self.__piezas__
    
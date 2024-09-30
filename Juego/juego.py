from Juego.tablero import Tablero

class Juego:
    
    def __init__(self, jugador1, jugador2):
        self.__estado__ = True
        self.__tablero__ = Tablero()
        self.__blanco__ = jugador1
        self.__negro__ = jugador2
        self.__turno__ = self.__blanco__


    # Metodo para cambiar los turnos luego de cada jugada
    def cambiar_turno(self):
        if self.__turno__ == self.__blanco__:
            self.__turno__ = self.__negro__
        else:
            self.__turno__ = self.__blanco__


    # Metodo que permite finalizar el juego, estableciendo el atributo estado en 0 (No Jugando) 
    def terminar_juego(self):
        self.__estado__ = False
        return self.__tablero__
    
    #Metodo para ver si algun jugador gano la partida, o porque comio todas las piezas del rival o porque hay jaque mate
    def ganar_juego(self, color):
        if self.__tablero__.jaque_mate_tablero(color): # caso en el que algun jugador haga jaque mate
            jugador = self.__negro__ if color == 'blanco' else self.__blanco__
            return f'---  El rey {color} esta en jaque mate, por lo tanto {jugador} es el ganador!! ---'
        else:
            pass


    # Metodo para mover pieza, donde se ingresa la posicion donde se desea mover y que pieza,
    #lo que hace este metodo es llamar al metodo de mover_pieza_tablero para que la pieza
    #se mueva en el tablero
    def mover_pieza(self, x, y, pieza): 
        y = y.upper()
        if self.__tablero__.mover_pieza_tablero(x, y, pieza):
            color = 'blanco' if self.__turno__ == self.__negro__ else 'negro' 
            return self.ganar_juego(color)
        else:
            raise ValueError('Movimiento no valido')
  
    #Metodo que verifica si la pieza existe
    def existe_pieza(self, pieza):
        turno = 'blanco' if self.__turno__ == self.__blanco__ else 'negro'
        pieza_original = pieza + ' ' + turno
        if pieza_original not in self.__tablero__.piezas:  # Se verifica si la pieza existe
            raise ValueError(f'{pieza} no existe')
        else:
            return pieza_original
        
    
    def verificar_entrada(self, x, y):
        return self.verificar_fila(x) and self.verificar_columna(y)
    
    def verificar_fila(self, x):
        x = int(x)
        if (1 <= x <= 8):
            return True
        else:
            return False
        
    def verificar_columna(self, y):
        y = y.upper()
        fila1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        if y in fila1:
            return True
        else:
            return False
    
    #Metodo para poder ver el estado del juego (encapsulamiento)
    @property
    def estado(self):
        return self.__estado__
    
    #Metodo para poder ver el tablero del juego 
    @property
    def tablero(self):
        return self.__tablero__
    
    @tablero.setter
    def tablero(self, value):
        self.__tablero__ = value
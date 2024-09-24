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
        if self.tablero.quedan_piezas() == 'Blanco': # si no quedan piezas blancas gana negro
            return f'{self.__negro__} es el ganador'
        elif self.tablero.quedan_piezas() == 'Negro': # si no quedan piezas negras gana blanco
            return f'{self.__blanco__} es el ganador'
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
  
    #Metodo que verifica si la pieza existe
    def existe_pieza(self, pieza):
        turno = 'blanco' if self.__turno__ == self.__blanco__ else 'negro'
        pieza_original = pieza + ' ' + turno
        if not self.tablero.pieza_existente(pieza_original):
            raise ValueError(f'{pieza} no existe')
        else:
            return pieza_original
        
    # Metodo que verifica si la fila es correcta
    def verificar_fila(self, x):
        x = int(x)
        if not (1 <= x <= 8):
            raise ValueError (f'La fila {x} no existe')
        else:
            return x



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
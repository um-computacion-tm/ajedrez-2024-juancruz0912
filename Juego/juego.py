from .tablero import Tablero


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
        elif self.tablero.jaque_mate_tablero(color): # caso en el que algun jugador haga jaque mate
            jugador = self.__negro__ if color == 'blanco' else self.__blanco__
            return f'---  El rey {color} esta en jaque mate, por lo tanto {jugador} es el ganador!! ---'
        else:
            pass
        

    # Metodo para mover pieza, donde se ingresa la posicion donde se desea mover y que pieza,
    #lo que hace este metodo es llamar al metodo de mover_pieza_tablero para que la pieza
    #se mueva en el tablero
    def mover_pieza(self, x, y, pieza): 
        turno = 'blanco' if self.__turno__ == self.__blanco__ else 'negro'
        pieza_original = pieza + ' ' + turno
        if not self.__tablero__.pieza_existente(pieza_original):
            raise ValueError(f'{pieza} no existe')
        else:
            
            y = y.upper()
            if self.__tablero__.mover_pieza_tablero(x, y, pieza_original):
                color = 'blanco' if turno == 'negro' else 'negro' # Si el movimiento de la pieza es correcto, cambia el turno
                return self.ganar_juego(color)
  
    
    
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
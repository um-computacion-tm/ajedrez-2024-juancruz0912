from .Tablero import Tablero

class Juego:
    
    def __init__(self, jugador1, jugador2):
        self.__estado__ = False
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

    # Metodo que permite iniciar el juego, estableciendo el atributo estado en 1 (Jugando)
    def empezar_juego(self):
        self.__estado__ = True
        return self.__tablero__

    # Metodo que permite finalizar el juego, estableciendo el atributo estado en 0 (No Jugando) 
    def terminar_juego(self):
        self.__estado__ = False
        return self.__tablero__

    # Metodo para mover pieza, donde se ingresa la posicion donde se desea mover y que pieza,
    #lo que hace este metodo es llamar al metodo de mover_pieza_tablero para que la pieza
    #se mueva en el tablero
    def mover_pieza(self, x, y, pieza): 
        turno = 'blanco' if self.__turno__ == self.__blanco__ else 'negro'
        pieza = pieza + ' ' + turno
        self.__tablero__.mover_pieza_tablero(x, y, pieza)
        return self.__tablero__

    def buscar_pieza(self, pieza):
        turno = 'blanco' if self.__turno__ == self.__blanco__ else 'negro'
        pieza = str(pieza + ' ' + turno)
        return self.tablero.pieza_existente(pieza)   
    
    #Metodo para poder ver el estado del juego (encapsulamiento)
    @property
    def estado(self):
        return self.__estado__
    
    #Metodo para poder ver el tablero del juego 
    @property
    def tablero(self):
        return self.__tablero__
from Tablero import Tablero

class Juego:
    def __init__(self, jugador1, jugador2):
        self.__estado__ = False
        self.__tablero__ = Tablero()
        self.__blanco__ = jugador1
        self.__negro__ = jugador2
        self.__turno__ = jugador1

    #Metodo para cambiar los turnos luego de cada jugada
    def cambiar_turno(self):
        if self.__turno__ == self.__blanco__:
            self.__turno__ = self.__negro__
        else:
            self.__turno__ = self.__blanco__

    #Metodo que permite iniciar el juego, estableciendo el atributo estado en 1 (Jugando)
    def empezar_juego(self):
        self.__estado__ = True
        print('Empezo el juego')
        self.__tablero__.imprimir_tablero()

    #Metodo que permite finalizar el juego, estableciendo el atributo estado en 0 (No Jugando) 
    def terminar_juego(self):
        self.__estado__ = False
        print("Se termino el juego")
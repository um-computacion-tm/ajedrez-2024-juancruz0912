class Juego:
    def __init__(self, tablero, jugador1, jugador2):
        self.__estado__ = 0
        self.__tablero__ = tablero
        self.__blanco__ = jugador1
        self.__negro__ = jugador2
        self.__turno__ = jugador1


    #Metodo que permite iniciar el juego, estableciendo el atributo estado en 1 (Jugando)
    def empezar_juego(self):
        self.__estado__ = 1
        print('Empezo el juego')

    #Metodo que permite finalizar el juego, estableciendo el atributo estado en 0 (No Jugando) 
    def terminar_juego(self):
        self.__estado__ = 0
        print("Se termino el juego")
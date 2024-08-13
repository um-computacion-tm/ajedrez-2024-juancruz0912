from Clases.Juego import Juego

def main():
    
    print('Bienvenidos al juego del ajedrez')
    print('Ingresar los nombres de los jugadores')
    
    jugador1 = input('Jugador 1: ')
    jugador2 = input('Jugador 2: ')
    juego = Juego('tablero', jugador1, jugador2)
    juego.empezar_juego()
    
    while juego.__estado__ == 1:
        estado = int(input('Ingresar 1 para seguir jugando o 0 para terminar el juego'))
        if estado == 0:
            juego.terminar_juego()

main()
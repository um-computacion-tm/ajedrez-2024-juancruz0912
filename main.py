from Clases.Juego import Juego

def main():
    
    print('Bienvenidos al juego del ajedrez')
    print('Ingresar los nombres de los jugadores')
    
    jugador1 = input('Jugador 1: ')
    jugador2 = input('Jugador 2: ')
    juego = Juego(jugador1, jugador2)
    juego.empezar_juego()
    
    while juego.estado == True:
        print(juego.tablero)
        print(f'Ahora es el turno de {juego.__turno__}')
        pieza = input('Que pieza quieres mover?')
        
        if pieza == '0':
            juego.terminar_juego()
        else:    
            fila = int(input('Fila donde quieres mover la pieza: '))
            columna = int(input('Columna donde quieres mover la pieza: '))
            try:
                juego.mover_pieza(fila, columna, pieza)
            except ValueError:
                pass
            juego.cambiar_turno()


if __name__ == '__main__':
    main()
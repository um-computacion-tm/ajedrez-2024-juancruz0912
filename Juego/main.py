from .Clases.Juego import Juego
import os

def jugar(juego):
        try:
            print(juego.tablero)
            print(f'\nAhora es el turno de {juego.__turno__}')
            mover(juego)            
        except Exception as e:
            print("error", e)

def mover(juego):
    pieza = input('Que pieza quieres mover?: ')
    if pieza == '0':
        juego.terminar_juego()
    elif juego.buscar_pieza(pieza) == True:
        mover_pieza_valida(juego, pieza)
    else:  
        print(f'{pieza} no existe') 
        mover(juego)

def mover_pieza_valida(juego, pieza):
    fila = int(input('Fila donde quieres mover la pieza: '))
    columna = input('Columna donde quieres mover la pieza: ')
    try:
        juego.mover_pieza(fila, columna, pieza)
        juego.cambiar_turno()
    except ValueError as e:
        print(e)
        mover_pieza_valida(juego, pieza)

def limpiar_pantalla():
    if os.name == 'posix':  
        os.system('clear')



def main():
    
    limpiar_pantalla()
    print('------ Bienvenidos al juego del ajedrez -------- \n')
    print('- En todo momento que quieras terminar el juego, escribe 0 en vez de ingresar el nombre de la pieza\n')
    print(' - Ingresar los nombres de los jugadores -\n')
    
    jugador1 = input('Jugador 1 (Blancas): ')
    jugador2 = input('Jugador 2 (Negras): ')
    juego = Juego(jugador1, jugador2)
    juego.empezar_juego()
    
    while juego.estado == True:
        jugar(juego)
    print('Se termino el juego')

if __name__ == '__main__':
    main()
from .juego import Juego
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
    pieza = pieza.capitalize()
    if pieza == '0':
        juego.terminar_juego()
    else:
        try:
            mover_pieza_valida(juego, pieza)
        except Exception as e:
            print(e)
            mover(juego)

def mover_pieza_valida(juego, pieza):
    try:
        fila = int(input('Fila donde quieres mover la pieza (o 0 para cancelar): '))
        if fila == 0:
            mover(juego)  
            return 
    except ValueError:
        print('La fila no es un número válido.')
        mover_pieza_valida(juego, pieza)  
        return
    columna = input('Columna donde quieres mover la pieza (o 0 para cancelar): ')
    if columna == '0':
        mover(juego) 
        return  
    mensaje = juego.mover_pieza(fila, columna, pieza)
    if mensaje:
        print(juego.tablero)
        print(mensaje)
        juego.terminar_juego() 
    else:
        juego.cambiar_turno()



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
    
    while juego.estado == True:
        jugar(juego)
    
    print('Se termino el juego')

if __name__ == '__main__':
    main()
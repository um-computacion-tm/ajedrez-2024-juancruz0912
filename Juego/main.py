from Juego.juego import Juego
import os

def jugar(juego):
        try:
            limpiar_pantalla()
            print(juego.tablero)
            print(f'\nAhora es el turno de {juego.__turno__}')
            mover(juego)            
        except Exception as e:
            print(e)

def mover(juego):
    pieza = input('Que pieza quieres mover? (0 para terminar): ')
    pieza = pieza.capitalize()
    if pieza == '0':
        juego.terminar_juego()
    else:
        try:
            pieza = juego.existe_pieza(pieza)
            mover_pieza_valida(juego, pieza)
        except Exception as e:
            print(e)
            mover(juego)

def mover_pieza_valida(juego, pieza):
    entrada = (input('Posicion donde quieres mover la pieza (Ej: "c6" o 0 para cancelar): '))
    if entrada == 0:
        mover(juego)
        return
    try:
        fila = juego.verificar_fila(entrada[1])
    except ValueError:
        print('La fila no es un número válido.')
        mover_pieza_valida(juego, pieza)  
        return
    columna = entrada[0]
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
    
    
    print('------ Bienvenidos al juego del ajedrez -------- \n')
    print('- En todo momento que quieras terminar el juego, escribe 0 en vez de ingresar el nombre de la pieza - \n')
    print(' - Ingresar los nombres de los jugadores -\n')
    
    jugador1 = input('Jugador 1 (Blancas): ')
    jugador2 = input('Jugador 2 (Negras): ')
    juego = Juego(jugador1, jugador2)
    
    while juego.estado == True:
        jugar(juego)
    
    print('Se termino el juego')

if __name__ == '__main__':
    main()
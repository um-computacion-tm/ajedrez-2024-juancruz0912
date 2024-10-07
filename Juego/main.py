from Juego.juego import Juego
import os

def jugar(juego):
        try:
            print(juego.tablero)
            print(f'\nAhora es el turno de {juego.__turno__}')
            mover(juego)            
        except Exception as e:
            print(e)

def mover(juego):
    pieza = input('Que pieza quieres mover? (o 0 para terminar): ')
    pieza = pieza.capitalize()
    if pieza == '0':
        juego.terminar_juego()
    else:
        try:
            pieza = juego.existe_pieza(pieza)
            verificar_entrada(juego, pieza)
        except Exception as e:
            print(e)
            mover(juego)

def verificar_entrada(juego, pieza):
    entrada_valida = True
    try:
        while entrada_valida:
            entrada = (input('Posicion donde quieres mover la pieza (o 0 para cancelar): '))
            if entrada == 0:
                mover(juego)
            elif len(entrada) != 2:
                print('La posición no es válida.')
                verificar_entrada(juego, pieza)
            elif not juego.verificar_fila(entrada[1]):
                print('La fila no es válida.')
            elif not juego.verificar_columna(entrada[0]):
                print('La columna no es válida.')
            else:
                entrada_valida = False
    except Exception:
        print('La entrada no es valida')
        verificar_entrada(juego, pieza)
    fila = int(entrada[1])
    columna = entrada[0]
    mover_pieza_valida(juego, pieza, fila, columna)

def mover_pieza_valida(juego, pieza, fila, columna):
    mensaje = juego.mover_pieza(fila, columna, pieza)
    if mensaje:
        print(juego.tablero)
        print(mensaje)
        juego.terminar_juego() 
    else:
        juego.cambiar_turno()




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
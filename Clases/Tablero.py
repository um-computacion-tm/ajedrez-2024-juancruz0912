
class Tablero:
    def __init__(self):
        self.__tablero__ = [[" " for i in range(9)] for i in range(9)]
        self.__tablero__[0] = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
        self.__tablero__[1] = [" ", '', "♘", "♗", "♕", "♔", "♗", "♘", "♖"]  
        self.__tablero__[1][1] = Torre("negro", 1)
        self.__tablero__[2] = [" "] + ["♙"] * 8 
        self.__tablero__[7] = [" "] + ["♟︎"] * 8 
        self.__tablero__[8] = [" ", "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]

        for i in range(9,1):
            self.__tablero__[i][0] = str(i)
        
    
    #Metodo para mostrar el tablero en la terminal
    def imprimir_tablero(self):
        print("   " + " | ".join(self.__tablero__[0][1:]) + " |")
        for fila in self.__tablero__[1:]:
            fila_str = [str(celda) if celda is not None else "   " for celda in fila]
            print(" | ".join(fila_str) + " |")
            linea = '--+' + '---+' * (len(fila) - 1)
            print(linea)


    #Metodo para ver el contenido de una celda en espedifico, lo inputs son el numero de fila y de columna
    def ver_celda(self, fila, columna):
        if self.__tablero__[fila][columna] == ' ':
            mensaje = 'vacio'
        else:   
            mensaje = self.__tablero__[fila][columna]
        
        print(f'en la cela {fila},{columna} se encuentra : {mensaje}')
        return mensaje


    def mover_pieza(self, xo, yo, xd, yd):
        self.__tablero__[xd][yd] = self.__tablero__[xo][yo]
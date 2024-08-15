class Tablero:
    def __init__(self):
        self.__tablero__ = [[" " for i in range(9)] for i in range(9)]
        self.__tablero__[0] = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
        self.__tablero__[1] = [" ","T", "C", "A", "Q", "K", "A", "C", "T"]
        self.__tablero__[2] = [" "] + ["P"] * 8
        self.__tablero__[7] = [" "] + ["P"] * 8
        self.__tablero__[8] = [" ","T", "C", "A", "Q", "K", "A", "C", "T"]
        for i in range(1,9):
            self.__tablero__[i][0] = str(i)
        
    
    #Metodo para mostrar el tablero en la terminal
    def imprimir_tablero(self):
        for fila in self.__tablero__:
            linea = '--+' + '---+' * 8  
            print(" | ".join(fila)+ " |")
            print(linea)

    #Metodo para ver el contenido de una celda en espedifico, lo inputs son el numero de fila y de columna
    def ver_celda(self, fila, columna):
        if self.__tablero__[fila][columna] == ' ':
            mensaje = 'vacio'
        else:   
            mensaje = self.__tablero__[fila][columna]
        
        print(f'en la cela {fila},{columna} se encuentra : {mensaje}')
        return mensaje

    #Metodo para mover una pieza, donde se ingresan las variables x(fila), y(columna) y pieza(pieza a mover)
    def mover_pieza(self, x, y, pieza):
        self.__tablero__[x][y] = pieza







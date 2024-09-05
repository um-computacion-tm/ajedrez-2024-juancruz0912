import unittest
from Juego.Clases.Tablero import Tablero
from Juego.Clases.Piezas.Torre import Torre
from Juego.Clases.Piezas.Peon import Peon
from Juego.Clases.Piezas.Alfil import Alfil
from Juego.Clases.Piezas.Caballo import Caballo

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()
        self.tablero.tablero[4][4] = '  '  # Limpiar casilla central para pruebas
        self.torre_blanca = self.tablero.piezas['Torre 1 blanco'] 
        self.peon_blanco = self.tablero.piezas['Peon 1 blanco']
        self.alfil_blanco = self.tablero.piezas['Alfil 2 blanco']
        self.caballo_blanco = self.tablero.piezas['Caballo 1 blanco']
        self.torre_negra = self.tablero.piezas['Torre 2 negro']
        self.peon_negro = self.tablero.piezas['Peon 5 negro']
        self.rey_blanco = self.tablero.piezas['Rey blanco']
        self.rey_negro = self.tablero.piezas['Rey negro']

    # Verificar que todas las piezas han sido creadas
    def test_crear_piezas(self):
        piezas = self.tablero.__piezas__
        self.assertEqual(len(piezas), 32)
        self.assertIsInstance(piezas['Torre 1 negro'], Torre)

    # Verificar que las piezas están en la posición correcta después de colocarlas
    def test_colocar_piezas(self):
        pieza = self.tablero.tablero[1][1]
        self.assertIsInstance(pieza, Torre)

    # Este test solo verifica que la función se ejecuta sin errores
    def test_imprimir_tablero(self):   
        try:
            print(self.tablero)
        except Exception as e:
            self.fail(f"imprimir_tablero lanzó una excepción: {e}")

    # Verificacion del metodo para mover fichas rectas
    def test_movimiento_recto_valido_horizontal(self):
        self.tablero.tablero[1][2] = '  '
        self.tablero.movimiento_recto_valido(1, 2, self.tablero.piezas['Torre 1 negro'])
        self.assertIsInstance(self.tablero.tablero[1][2], Torre)  

    # Ingresar una fila que no es del tablero
    def test_movimiento_fila_invalida(self):
        self.tablero.tablero[7][5] = '  '
        self.tablero.tablero[8][5] = '  '
        with self.assertRaises(ValueError) as context:
            self.tablero.mover_pieza_tablero(9, 'A', self.torre_negra)
        self.assertIn('La fila 9 no existe', str(context.exception))

    def test_columna_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.mover_pieza_tablero(7, 'Z', self.torre_blanca)  # Movimiento no válido
        self.assertIn('La columna Z no existe', str(context.exception))
    
    def test_movimiento_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.mover_pieza_tablero(7, 'A', 'Caballo 1 blanco')
        self.assertIn('Movimiento no valido', str(context.exception))
    
    # Movimiento que no es recto
    def test_movimiento_recto_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.movimiento_recto_valido(7, 6, self.torre_blanca)  # Movimiento no válido
        self.assertIn('El movimiento debe ser en vertical o horizontal', str(context.exception))
    
    # Test donde en un movimiento recto la casilla está ocupada
    def test_movimiento_recto_ocupado(self):  
        with self.assertRaises(ValueError) as context:
            self.tablero.movimiento_recto_valido(4, 1, self.torre_blanca)
        self.assertIn('La casilla 7,1 esta ocupada por una pieza del mismo color', str(context.exception))

    # Verificando el movimiento diagonal válido
    def test_mover_pieza_tablero_diagonal(self):
        self.tablero.tablero[7][2] = '  '  
        self.tablero.mover_pieza_tablero(6, 'A', 'Alfil 1 blanco')
        self.assertIsInstance(self.tablero.tablero[6][1], Alfil)

    # Test donde en un movimiento diagonal la casilla está ocupada
    def test_movimiento_diagonal_ocupado(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.movimiento_diagonal_valido(6, 8, self.alfil_blanco)
        self.assertIn('La casilla 7,7 esta ocupada por una pieza del mismo color', str(context.exception))

    # Verificando el movimiento del caballo
    def test_mover_pieza_tablero_caballo(self):
        self.tablero.mover_pieza_tablero(6, 'C', 'Caballo 1 blanco')
        self.assertIsInstance(self.tablero.tablero[6][3], Caballo)

    def test_movimiento_peon_invalido(self):
        with self.assertRaises(ValueError) as context: 
            self.tablero.mover_pieza_tablero(3, 'B', 'Peon 1 negro')
        self.assertIn('El peon solo se puede mover en línea recta', str(context.exception))

    # Verificar que se puede mover una pieza correctamente
    def test_mover_pieza_tablero(self):        
        self.tablero.mover_pieza_tablero(5, 'A', 'Peon 1 blanco')
        self.assertIsInstance(self.tablero.tablero[5][1], Peon)

    # Mover pieza al mismo lugar
    def test_mismo_lugar(self):
        with self.assertRaises(ValueError) as context: 
            self.tablero.mover_pieza_tablero(1, 'A', 'Torre 1 negro')
        self.assertIn('La pieza no se ha movido', str(context.exception))

    # Mover pieza a una posición ocupada por una pieza de su mismo color
    def test_mover_pieza_tablero_cassilla_ocupada(self):
        self.tablero.__tablero__[7][1] = self.torre_blanca  
        with self.assertRaises(ValueError) as context: 
            self.tablero.mover_pieza_tablero(3, 'A', 'Torre 1 blanco')
        self.assertEqual(str(context.exception), 'La casilla 7,1 esta ocupada por una pieza del mismo color')

    # Test donde la torre blanca come al peon negro, se verifica que la torre se movió y que el peon no está más en la lista
    def test_comer_pieza(self):
        self.tablero.__tablero__[4][4] = self.torre_blanca
        self.tablero.__tablero__[5][4] = self.peon_negro
        self.torre_blanca.fila = 4
        self.torre_blanca.columna = 4
        self.tablero.comer_pieza(5, 4, self.torre_blanca)        
        self.assertIsInstance(self.tablero.__tablero__[5][4], Torre)
        self.assertEqual(self.tablero.__tablero__[4][4], '  ')
        self.assertNotIn('Peon 5 negro', self.tablero.__piezas__)

    def test_comer_pieza_horizontal(self):
        self.tablero.__tablero__[4][6] = self.torre_blanca
        self.tablero.__tablero__[4][4] = self.peon_negro
        self.torre_blanca.fila = 4
        self.torre_blanca.columna = 6
        self.tablero.movimiento_horizontal(4, 4, self.torre_blanca)      
        self.assertIsInstance(self.tablero.__tablero__[4][4], Torre)
        self.assertEqual(self.tablero.__tablero__[4][6], '  ')

    # Test el caballo come una pieza
    def test_comer_pieza_caballo(self):
        self.peon = self.tablero.piezas['Peon 2 negro']
        self.tablero.tablero[6][3] = self.peon
        self.tablero.mover_pieza_tablero(6, 'C', 'Caballo 1 blanco')
        self.assertIsInstance(self.tablero.__tablero__[6][3], Caballo)
        self.assertEqual(self.tablero.__tablero__[8][2], '  ')
        self.assertNotIn('Peon 2 negro', self.tablero.__piezas__)

    # Test el peon come una pieza
    def test_comer_pieza_peon(self):
        self.peon = self.tablero.piezas['Peon 2 negro']
        self.tablero.tablero[6][3] = self.peon
        self.tablero.mover_pieza_tablero(6, 'C', 'Peon 2 blanco')
        self.assertIsInstance(self.tablero.__tablero__[6][3], Peon)
        self.assertEqual(self.tablero.__tablero__[7][2], '  ')
        self.assertNotIn('Peon 2 negro', self.tablero.__piezas__)

    # Intentamos que una pieza blanca coma a otra pieza blanca (debe lanzar una excepción)
    def test_comer_pieza_invalido(self):
        self.tablero.__tablero__[6][4] = self.alfil_blanco
        with self.assertRaises(ValueError) as context:
            self.tablero.comer_pieza(6, 4, self.torre_blanca)
        self.assertIn('La casilla 6,4 esta ocupada por una pieza del mismo color', str(context.exception))


if __name__ == '__main__':
    unittest.main()

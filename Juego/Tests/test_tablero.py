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
        self.torre = Torre('blanco', 1, 4, 4)
        self.alfil = Alfil('blanco', 1, 8, 3)
       

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

    # Verificacion del metodo para mover fichas rectas, en forma horizontal y vertical
    def test_movimiento_recto_valido_horizontal(self):
        self.assertTrue(self.tablero.movimiento_recto_valido(4, 6, self.torre))  # Movimiento horizontal 

    def test_movimiento_recto_valido_vertical(self):
        self.assertTrue(self.tablero.movimiento_recto_valido(6, 4, self.torre))  # Movimiento vertical 

    def test_movimiento_recto_invalido(self):
        with self.assertRaises(ValueError):
            self.tablero.movimiento_recto_valido(7, 7, self.torre)  # Movimiento no válido
    
    # Test donde en un movimiento recto la casilla esta ocupada
    def test_movimiento_recto_ocupado(self):
        self.tablero.tablero[4][5] = '♖ '  # Colocar pieza en el camino
        with self.assertRaises(ValueError) as context:
            self.tablero.movimiento_recto_valido(4, 7, self.torre)
        self.assertIn('esta ocupada', str(context.exception))

    #Metodo para verificar si el movimiento de la pieza es diagonal
    def test_movimiento_diagonal_valido(self):
        self.tablero.tablero[7][2] = '  ' # Limpiar casilla
        self.tablero.movimiento_diagonal_valido(6, 1, self.alfil)
        self.assertIsInstance(self.tablero.tablero[6][1], Alfil)  # Movimiento diagonal válido

    # Test donde en un movimiento diagonal la casilla esta ocupada
    def test_movimiento_diagonal_ocupado(self):
        self.tablero.tablero[5][2] = '♝ '  # Colocar pieza en el camino
        with self.assertRaises(ValueError) as context:
            self.tablero.movimiento_diagonal_valido(6, 1, self.alfil)
        self.assertIn('esta ocupada', str(context.exception))

    # Verificar que se puede mover una pieza correctamente
    def test_mover_pieza_tablero(self):        
        self.tablero.mover_pieza_tablero(5, 'A', 'Peon 1 blanco')
        celda_nueva = self.tablero.tablero[5][1]
        self.assertIsInstance(celda_nueva, Peon)
        celda_original = self.tablero.tablero[7][1]
        self.assertEqual(celda_original, '  ')

    def test_mover_pieza_tablero_movimiento(self):
        with self.assertRaises(ValueError) as context: # pieza ocupada
            self.tablero.mover_pieza_tablero(3, 'A', 'Torre 1 blanco')
        self.assertEqual(str(context.exception), 'La casilla 8,1 esta ocupada')

    def test_mover_pieza_tablero_diagonal(self):
        self.tablero.tablero[7][2] = '  ' # Limpiar casilla
        self.tablero.mover_pieza_tablero(6, 'A', 'Alfil 1 blanco')
        self.assertEqual(self.tablero.tablero[8][3], '  ')
        self.assertIsInstance(self.tablero.tablero[6][1], Alfil)

    def test_mover_pieza_tablero_caballo(self):
        self.tablero.mover_pieza_tablero(6, 'C', 'Caballo 1 blanco')
        self.assertEqual(self.tablero.tablero[8][2], '  ')
        self.assertIsInstance(self.tablero.tablero[6][3], Caballo)


    def test_pieza_existente(self):
        self.assertTrue(self.tablero.pieza_existente('Caballo 2 blanco'))
        self.assertFalse(self.tablero.pieza_existente('Torre 4 negro'))


if __name__ == '__main__':
    unittest.main()
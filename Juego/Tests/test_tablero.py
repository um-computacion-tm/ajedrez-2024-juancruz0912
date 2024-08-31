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
        self.peon = Peon('blanco', 9, 4, 6)
        self.torre_blanca = Torre('blanco', 3, 4, 4)
        self.peon_negro = Peon('negro', 5, 5, 4)
        self.alfil_blanco = Alfil('blanco', 2, 6, 4)
        self.caballo_blanco = Caballo('blanco', 3, 3, 3)
        self.peon_negro2 = Peon('negro', 9, 6, 4) 
        self.torre_negra = Torre('negro', 5, 6, 5)

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
        self.assertTrue(self.tablero.movimiento_recto_valido(4, 6, self.torre))  

    # Movimiento que no es recto
    def test_movimiento_recto_invalido(self):
        with self.assertRaises(ValueError):
            self.tablero.movimiento_recto_valido(7, 7, self.torre)  # Movimiento no válido
    
    # Test donde en un movimiento recto la casilla esta ocupada
    def test_movimiento_recto_ocupado(self):  
        self.tablero.tablero[4][6] = self.peon
        with self.assertRaises(ValueError) as context:
            self.tablero.movimiento_recto_valido(4, 7, self.torre)
        self.assertIn('La casilla 4,6 esta ocupada', str(context.exception))

    # Verificando el movimiento diagonal valido
    def test_mover_pieza_tablero_diagonal(self):
        self.tablero.tablero[7][2] = '  ' # Limpiar casilla
        self.tablero.mover_pieza_tablero(6, 'A', 'Alfil 1 blanco')
        self.assertEqual(self.tablero.tablero[8][3], '  ')
        self.assertIsInstance(self.tablero.tablero[6][1], Alfil)

    # Test donde en un movimiento diagonal la casilla esta ocupada
    def test_movimiento_diagonal_ocupado(self):
        self.tablero.tablero[5][2] = '♝ '  # Colocar pieza en el camino
        with self.assertRaises(ValueError) as context:
            self.tablero.movimiento_diagonal_valido(6, 1, self.alfil)
        self.assertIn('esta ocupada', str(context.exception))

    # Verificando el movimiento del caballo
    def test_mover_pieza_tablero_caballo(self):
        self.tablero.mover_pieza_tablero(6, 'C', 'Caballo 1 blanco')
        self.assertEqual(self.tablero.tablero[8][2], '  ')
        self.assertIsInstance(self.tablero.tablero[6][3], Caballo)

    # Verificar que se puede mover una pieza correctamente
    def test_mover_pieza_tablero(self):        
        self.tablero.mover_pieza_tablero(5, 'A', 'Peon 1 blanco')
        celda_nueva = self.tablero.tablero[5][1]
        self.assertIsInstance(celda_nueva, Peon)
        celda_original = self.tablero.tablero[7][1]
        self.assertEqual(celda_original, '  ')

    # Mover pieza al mismo lugar
    def test_mismo_lugar(self):
        with self.assertRaises(ValueError) as context: 
            self.tablero.mover_pieza_tablero(1, 'A', 'Torre 1 negro')
        self.assertIn(str(context.exception), 'La pieza no se ha movido')

    # Mover pieza a una posicion ocupada por una pieza de su mismo color
    def test_mover_pieza_tablero_movimiento(self):
        with self.assertRaises(ValueError) as context: 
            self.tablero.mover_pieza_tablero(3, 'A', 'Torre 1 blanco')
        self.assertEqual(str(context.exception), 'La casilla 7,1 esta ocupada por una pieza del mismo color')

    # Test donde la torre blanca come al peon negro, se verifica que la torre se movio y qwue el peon no esta mas en la lista
    def test_comer_pieza(self):
        self.tablero.__piezas__['Torre 3 blanco'] = self.torre_blanca
        self.tablero.__tablero__[4][4] = self.torre_blanca

        self.tablero.__piezas__['Peon 5 negro'] = self.peon_negro
        self.tablero.__tablero__[5][4] = self.peon_negro

        self.tablero.comer_pieza(5, 4, self.torre_blanca)

        self.assertIsInstance(self.tablero.__tablero__[5][4], Torre)
        self.assertEqual(self.tablero.__tablero__[4][4], '  ')
        self.assertNotIn('Peon 5 negro', self.tablero.__piezas__)

    # Intentamos que una pieza blanca coma a otra pieza blanca (debe lanzar una excepción)
    def test_comer_pieza_invalido(self):
        self.tablero.__piezas__['Alfil 2 blanco'] = self.alfil_blanco
        self.tablero.__tablero__[6][4] = self.alfil_blanco
        with self.assertRaises(ValueError) as context:
            self.tablero.comer_pieza(6, 4, self.torre_blanca)
        self.assertIn('esta ocupada por una pieza del mismo color', str(context.exception))

    # Verificar si funciona el metodo comer_pieza para caballo
    def test_mover_pieza_caballo(self):
        self.tablero.__piezas__['Caballo 3 blanco'] = self.caballo_blanco
        self.tablero.__tablero__[3][3] = self.caballo_blanco
        
        self.tablero.__piezas__['Peon 5 negro'] = self.peon_negro
        self.tablero.__tablero__[5][4] = self.peon_negro
        
        self.tablero.mover_pieza_tablero(5, 'D', 'Caballo 3 blanco')

        self.assertIsInstance(self.tablero.__tablero__[5][4], Caballo)
        self.assertEqual(self.tablero.__tablero__[3][3], '  ')
        self.assertNotIn('Peon 5 negro', self.tablero.__piezas__)

    # En forma vertical
    def test_movimiento_peon_comer_valido(self):
        self.tablero.__piezas__['Peon 9 negro'] = self.peon_negro2
        self.tablero.__tablero__[6][4] = self.peon_negro2

        self.tablero.mover_pieza_tablero(7, 'C', 'Peon 9 negro') # Mover donde se encuentra el Peon 3 blanco
        
        self.assertIsInstance(self.tablero.__tablero__[7][3], Peon)
        self.assertEqual(self.tablero.__tablero__[6][4], '  ')
        self.assertNotIn('Peon 3 blanco', self.tablero.__piezas__)
    
    def test_movimiento_peon_comer_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.mover_pieza_tablero(6, 'B', 'Peon 1 blanco')
        self.assertIn(str(context.exception), 'El peon solo se puede mover en línea recta')


    # Verifica si la pieza existe en el atributo __piezas__
    def test_pieza_existente(self):
        self.assertTrue(self.tablero.pieza_existente('Caballo 2 blanco'))
        self.assertFalse(self.tablero.pieza_existente('Torre 4 negro'))

if __name__ == '__main__':
    unittest.main()
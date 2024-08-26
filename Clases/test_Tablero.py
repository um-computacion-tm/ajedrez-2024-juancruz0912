import unittest
from .Tablero import Tablero
from .Piezas.Torre import Torre
from .Piezas.Peon import Peon

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    # Verificar que todas las piezas han sido creadas
    def test_crear_piezas(self):
        piezas = self.tablero.__piezas__
        self.assertEqual(len(piezas), 32)
        self.assertIsInstance(piezas['Torre 1 negro'], Torre)

    # Verificar que las piezas están en la posición correcta después de colocarlas
    def test_colocar_piezas(self):
        pieza = self.tablero.__tablero__[1][1]
        self.assertIsInstance(pieza, Torre)

        # Este test solo verifica que la función se ejecuta sin errores
    def test_imprimir_tablero(self):   
        try:
            print(self.tablero)
        except Exception as e:
            self.fail(f"imprimir_tablero lanzó una excepción: {e}")


    # Verificar que se puede mover una pieza correctamente
    def test_mover_pieza_tablero(self):        
        self.tablero.mover_pieza_tablero(5, 'A', 'Peon 1 blanco')
        celda_nueva = self.tablero.__tablero__[5][1]
        self.assertIsInstance(celda_nueva, Peon)
        celda_original = self.tablero.__tablero__[7][1]
        self.assertEqual(celda_original, '   ')

    def test_mover_pieza_tablero_movimiento(self):
        with self.assertRaises(ValueError) as context: # pieza ocupada
            self.tablero.mover_pieza_tablero(3, 'A', 'Torre 1 blanco')
        self.assertEqual(str(context.exception), 'La casilla 8,1 esta ocupada')


if __name__ == '__main__':
    unittest.main()
import unittest
from Juego.Clases.Piezas.Alfil import Alfil

class TestAlfil(unittest.TestCase):

    def setUp(self):
        self.alfil_negro = Alfil('negro', 1, 1, 3)
        self.alfil_blanco = Alfil('blanco', 1, 8, 3)

    def test_inicializacion(self):
        self.assertEqual(self.alfil_blanco.__str__(), '♗1')
        self.assertEqual(self.alfil_negro.__str__(), '♝1')
        self.assertEqual(self.alfil_blanco.__color__, 'blanco')
        self.assertEqual(self.alfil_negro.__color__, 'negro')

    def test_movimiento_valido(self):
        self.alfil_blanco.verificar_movimiento(6, 5)
        self.assertEqual(self.alfil_blanco.movimiento, 'Diagonal')
        self.alfil_negro.verificar_movimiento(3, 5)
        self.assertEqual(self.alfil_negro.movimiento, 'Diagonal')

    def test_movimiento_invalido(self):
        with self.assertRaises(ValueError):
            self.alfil_blanco.verificar_movimiento(8, 4)
        with self.assertRaises(ValueError):
            self.alfil_negro.verificar_movimiento(6, 3)

if __name__ == '__main__':
    unittest.main()

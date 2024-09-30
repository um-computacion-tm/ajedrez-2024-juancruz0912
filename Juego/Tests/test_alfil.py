import unittest
from Juego.Piezas.alfil import Alfil

class TestAlfil(unittest.TestCase):

    def setUp(self):
        self.alfil_negro = Alfil('negro', id =1)
        self.alfil_blanco = Alfil('blanco', id =1)

    def test_inicializacion(self):
        self.assertEqual(self.alfil_blanco.__str__(), '♗1')
        self.assertEqual(self.alfil_negro.__str__(), '♝1')
        self.assertEqual(self.alfil_blanco.__color__, 'blanco')
        self.assertEqual(self.alfil_negro.__color__, 'negro')

    def test_movimiento_valido(self):
        self.assertTrue(self.alfil_blanco.verificar_movimiento(6, 5))
        self.assertTrue(self.alfil_negro.verificar_movimiento(3, 5))

    def test_movimiento_invalido(self):
        self.assertFalse(self.alfil_blanco.verificar_movimiento(8, 4)) 
        self.assertFalse(self.alfil_negro.verificar_movimiento(6, 3))

if __name__ == '__main__':
    unittest.main()

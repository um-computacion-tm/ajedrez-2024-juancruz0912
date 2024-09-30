import unittest
from Juego.Piezas.caballo import Caballo

class TestCaballo(unittest.TestCase):

    def setUp(self):
        self.caballo_negro = Caballo('negro', id = 1)
        self.caballo_blanco = Caballo('blanco', id = 1)

    def test_inicializacion(self):
        self.assertEqual(self.caballo_blanco.__str__(), '♘1')
        self.assertEqual(self.caballo_negro.__str__(), '♞1')
        self.assertEqual(self.caballo_blanco.__color__, 'blanco')
        self.assertEqual(self.caballo_negro.__color__, 'negro')

    def test_movimiento_valido(self):
        self.assertTrue(self.caballo_blanco.verificar_movimiento(6, 3))
        self.assertTrue(self.caballo_negro.verificar_movimiento(3, 3))
        
    def test_movimiento_invalido(self):
        self.assertFalse(self.caballo_blanco.verificar_movimiento(6, 4))

if __name__ == '__main__':
    unittest.main()

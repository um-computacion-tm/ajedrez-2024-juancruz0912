import unittest
from Juego.Piezas.peon import Peon

class TestPeon(unittest.TestCase):

    def setUp(self):
        self.peon_negro = Peon('negro', id =1)
        self.peon_negro2 = Peon('negro', id = 2)
        self.peon_blanco = Peon('blanco', id = 1)
        self.peon_negro2.__primer_movimiento__ = True


    def test_inicializacion(self):
        self.assertEqual(self.peon_blanco.__str__(), '♙1')
        self.assertEqual(self.peon_negro.__str__(), '♟1')
        self.assertEqual(self.peon_blanco.__color__, 'blanco')
        self.assertEqual(self.peon_negro.__color__, 'negro')


    # Caso donde en la primer jugada se quieran mover mas de dos lugares
    def test_moverse_mas_lugares_blanco(self):
        self.assertFalse(self.peon_blanco.verificar_movimiento(4, 1))

    def test_moverse_mas_lugares_negro(self):
        self.assertFalse(self.peon_negro.verificar_movimiento(5, 1))

    def test_movimiento_valido_negro(self):
        self.peon_negro.verificar_movimiento(3, 1)
        self.assertTrue(self.peon_negro.verificar_movimiento(3, 1))

    def test_movimiento_invalido1_negro(self):
        self.assertFalse(self.peon_negro2.verificar_movimiento(6, 2))

    def test_movimiento_invalido2_negro(self):
        self.assertFalse(self.peon_negro2.verificar_movimiento(7, 3))

    def test_comer_peon(self):
        self.assertTrue(self.peon_negro2.verificar_movimiento(3, 3))


if __name__ == '__main__':
    unittest.main()

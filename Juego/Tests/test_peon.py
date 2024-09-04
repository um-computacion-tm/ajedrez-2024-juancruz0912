import unittest
from Juego.Clases.Piezas.Peon import Peon

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
        with self.assertRaises(ValueError) as context:
            self.peon_blanco.verificar_movimiento(4, 1)
        self.assertEqual(str(context.exception), 'El peon se puede mover una o dos casillas hacia adelante')

    def test_moverse_mas_lugares_negro(self):
        with self.assertRaises(ValueError) as context:
            self.peon_negro.verificar_movimiento(5, 1)
        self.assertEqual(str(context.exception), 'El peon se puede mover una o dos casillas hacia adelante')

    def test_movimiento_valido_negro(self):
        self.peon_negro.verificar_movimiento(3, 1)
        self.assertEqual(self.peon_negro.movimiento, 'Recto')
        self.assertTrue(self.peon_negro.verificar_movimiento(3, 1))

    def test_movimiento_invalido1_negro(self):
        with self.assertRaises(ValueError) as context:
            self.peon_negro2.verificar_movimiento(6, 2)
        self.assertEqual(str(context.exception), 'El peon se puede mover una casilla hacia adelante')

    def test_movimiento_invalido2_negro(self):
        with self.assertRaises(ValueError) as context:
            self.peon_negro2.verificar_movimiento(6, 3)
        self.assertEqual(str(context.exception), 'El peon solo se puede mover en línea recta')

    def test_comer_peon(self):
        movimiento = self.peon_negro2.verificar_movimiento(3, 3)
        self.assertTrue(movimiento)
        self.assertEqual(self.peon_negro2.movimiento, 'Comer')


if __name__ == '__main__':
    unittest.main()

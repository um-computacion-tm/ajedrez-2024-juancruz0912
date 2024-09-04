import unittest
from Juego.Clases.Piezas.Peon import Peon

class TestPeon(unittest.TestCase):

    def setUp(self):
        self.peon_negro = Peon('negro', id =1, fila = 2, columna = 1)
        self.peon_negro2 = Peon('negro', id = 2, fila =  4, columna =  2)
        self.peon_blanco = Peon('blanco', id = 1, fila = 7, columna = 1)
        self.peon_blanco2 = Peon('blanco', id = 2, fila = 5, columna = 2)
        self.peon_negro2.__primer_movimiento__ = True
        self.peon_blanco2.__primer_movimiento__ = True


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

    # Se inicia el peon mas adelante para verificar el movimiento luego del primer paso
    # Test piezas negras
    def test_movimiento_valido_negro(self):
        movimiento = self.peon_negro2.verificar_movimiento(5, 2)
        self.assertTrue(movimiento)
        self.assertEqual(self.peon_negro2.movimiento, 'Recto')

    def test_movimiento_invalido1_negro(self):
        with self.assertRaises(ValueError) as context:
            self.peon_negro2.verificar_movimiento(6, 2)
        self.assertEqual(str(context.exception), 'El peon se puede mover una casilla hacia adelante')

    def test_movimiento_invalido2_negro(self):
        with self.assertRaises(ValueError) as context:
            self.peon_negro2.verificar_movimiento(6, 3)
        self.assertEqual(str(context.exception), 'El peon solo se puede mover en línea recta')

    # Test piezas blancas
    def test_movimiento_valido_blanco(self):
        movimiento = self.peon_blanco2.verificar_movimiento(4, 2)
        self.assertTrue(movimiento)
        self.assertEqual(self.peon_blanco2.movimiento, 'Recto')

    def test_movimiento_invalido1_blanco(self):
        with self.assertRaises(ValueError) as context:
            self.peon_blanco2.verificar_movimiento(3, 2)
        self.assertEqual(str(context.exception), 'El peon se puede mover una casilla hacia adelante')

    def test_movimiento_invalido2_blanco(self):
        with self.assertRaises(ValueError) as context:
            self.peon_blanco2.verificar_movimiento(4, 5)
        self.assertEqual(str(context.exception), 'El peon solo se puede mover en línea recta')

    def test_comer_peon(self):
        movimiento = self.peon_blanco2.verificar_movimiento(4, 3)
        self.assertTrue(movimiento)
        self.assertEqual(self.peon_blanco2.movimiento, 'Comer')


if __name__ == '__main__':
    unittest.main()

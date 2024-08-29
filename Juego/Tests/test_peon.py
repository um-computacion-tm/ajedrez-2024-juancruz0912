import unittest
from Juego.Clases.Piezas.Peon import Peon

class TestPeon(unittest.TestCase):

    def setUp(self):
        self.peon_negro = Peon('negro', 1, 3, 1)
        self.peon_negro2 = Peon('negro', 2, 2, 2)
        self.peon_blanco = Peon('blanco', 1, 7, 1)
        self.peon_blanco2 = Peon('blanco', 2, 5, 2)


    def test_inicializacion(self):
        self.assertEqual(self.peon_blanco.__str__(), '♙1')
        self.assertEqual(self.peon_negro.__str__(), '♟1')
        self.assertEqual(self.peon_blanco.__color__, 'blanco')
        self.assertEqual(self.peon_negro.__color__, 'negro')

    # Primer movimiento
    def test_movimiento_valido_blanco(self):
        self.assertEqual(self.peon_blanco.verificar_movimiento(6, 1), 'Recto')
        self.assertEqual(self.peon_blanco.verificar_movimiento(5, 1), 'Recto')
        self.assertEqual(self.peon_negro2.verificar_movimiento(3, 2), 'Recto')
        self.assertEqual(self.peon_blanco2.verificar_movimiento(4, 2), 'Recto')


    # Se inicia el peon mas adelante para verificar el movimiento luego del primer paso
    def test_movimiento_valido_negro(self):
        self.assertEqual(self.peon_negro.verificar_movimiento(4, 1), 'Recto')

    
    def test_movimiento_invalido_blanco(self):
        with self.assertRaises(ValueError):
            self.peon_blanco.verificar_movimiento(4, 1)

    def test_movimiento_invalido_negro(self):
        with self.assertRaises(ValueError):
            self.peon_negro2.verificar_movimiento(5, 2)
    
    def test_movimiento_invalido(self):
        with self.assertRaises(ValueError):
            self.peon_negro.verificar_movimiento(3, 5)

if __name__ == '__main__':
    unittest.main()

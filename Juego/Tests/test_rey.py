import unittest
from Juego.Clases.Piezas.Rey import Rey

class TestRey(unittest.TestCase):

    def setUp(self):
        self.rey_negro = Rey('negro', 1, 5)
        self.rey_blanco = Rey('blanco', 8, 5)
        
    def test_inicializacion(self):
        self.assertEqual(self.rey_blanco.__str__(), '♔ ')
        self.assertEqual(self.rey_negro.__str__(), '♚ ')
        self.assertEqual(self.rey_blanco.__color__, 'blanco')
        self.assertEqual(self.rey_negro.__color__, 'negro')

    # Movimientos válidos dentro del rango del rey
    def test_movimiento_valido(self):

        movimiento_r = self.rey_blanco.verificar_movimiento(8, 6)
        self.assertEqual(movimiento_r, True)
        self.assertEqual(self.rey_blanco.movimiento, 'Recto')
        
        movimiento_a = self.rey_blanco.verificar_movimiento(7, 5)
        self.assertEqual(movimiento_a, True)
        self.assertEqual(self.rey_blanco.movimiento, 'Recto')
        
        movimiento_d = self.rey_blanco.verificar_movimiento(7, 6)
        self.assertEqual(movimiento_d, True)
        self.assertEqual(self.rey_blanco.movimiento, 'Diagonal')

    
    # Movimiento fuera del rango del rey
    def test_movimiento_invalido(self):
        self.assertFalse(self.rey_blanco.verificar_movimiento(8, 7))  # Movimiento fuera del rango del rey

if __name__ == '__main__':
    unittest.main()

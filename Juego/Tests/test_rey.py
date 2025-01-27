import unittest
from Juego.Piezas.rey import Rey

class TestRey(unittest.TestCase):

    def setUp(self):
        self.rey_negro = Rey('negro')
        self.rey_blanco = Rey('blanco')
        
    def test_inicializacion(self):
        self.assertEqual(self.rey_blanco.__str__(), '♔ ')
        self.assertEqual(self.rey_negro.__str__(), '♚ ')
        self.assertEqual(self.rey_blanco.__color__, 'blanco')
        self.assertEqual(self.rey_negro.__color__, 'negro')

    # Movimientos válidos dentro del rango del rey
    def test_movimiento_valido(self):

        self.assertTrue(self.rey_blanco.verificar_movimiento(8, 6))        
        self.assertTrue(self.rey_blanco.verificar_movimiento(7, 5))
        self.assertTrue(self.rey_blanco.verificar_movimiento(7, 6))

    
    # Movimiento fuera del rango del rey
    def test_movimiento_invalido(self):
        self.assertFalse(self.rey_blanco.verificar_movimiento(8, 7))  # Movimiento fuera del rango del rey

if __name__ == '__main__':
    unittest.main()

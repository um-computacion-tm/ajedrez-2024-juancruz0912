import unittest
from Juego.Piezas.reina import Reina

class TestReina(unittest.TestCase):

    def setUp(self):
        self.reina_negra = Reina('negro')
        self.reina_blanca = Reina('blanco')
        
    def test_inicializacion(self):
        self.assertEqual(self.reina_blanca.__str__(), '♕ ')
        self.assertEqual(self.reina_negra.__str__(), '♛ ')
        self.assertEqual(self.reina_blanca.__color__, 'blanco')
        self.assertEqual(self.reina_negra.__color__, 'negro')

    def test_movimiento_recto_valido(self):
        self.assertTrue(self.reina_blanca.verificar_movimiento(8, 7))

    def test_movimiento_diagonal_valido(self):
        self.assertTrue(self.reina_blanca.verificar_movimiento(7, 3))

    def test_movimiento_invalido(self):
            self.assertFalse(self.reina_blanca.verificar_movimiento(5, 6))  # Movimiento no válido

if __name__ == '__main__':
    unittest.main()

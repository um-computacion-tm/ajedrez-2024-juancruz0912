import unittest
from .Reina import Reina

class TestReina(unittest.TestCase):

    def setUp(self):
        self.reina_negra = Reina('negro', 0, 4)
        self.reina_blanca = Reina('blanco', 8, 4)
        
    def test_inicializacion(self):
        self.assertEqual(self.reina_blanca.__str__(), '♕ ')
        self.assertEqual(self.reina_negra.__str__(), '♛ ')
        self.assertEqual(self.reina_blanca.__color__, 'blanco')
        self.assertEqual(self.reina_negra.__color__, 'negro')

    def test_movimiento_recto_valido(self):
        self.assertEqual(self.reina_blanca.verificar_movimiento(8, 7), 'Recto')  # Misma fila
        self.assertEqual(self.reina_blanca.verificar_movimiento(5, 4), 'Recto')  # Misma columna

    def test_movimiento_diagonal_valido(self):
        self.assertEqual(self.reina_blanca.verificar_movimiento(7, 3), 'Diagonal')
        self.assertEqual(self.reina_blanca.verificar_movimiento(6, 6), 'Diagonal')

    def test_movimiento_igual_posicion(self):
        with self.assertRaises(ValueError):
            self.reina_blanca.verificar_movimiento(8, 4)

    def test_movimiento_invalido(self):
        with self.assertRaises(ValueError):
            self.reina_blanca.verificar_movimiento(5, 6)  # Movimiento no válido

if __name__ == '__main__':
    unittest.main()

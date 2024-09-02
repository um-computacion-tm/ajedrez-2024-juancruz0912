import unittest
from Juego.Clases.Piezas.Caballo import Caballo

class TestCaballo(unittest.TestCase):

    def setUp(self):
        self.caballo_negro = Caballo('negro', 1, 1, 2)
        self.caballo_blanco = Caballo('blanco', 1, 8, 2)

    def test_inicializacion(self):
        self.assertEqual(self.caballo_blanco.__str__(), '♘1')
        self.assertEqual(self.caballo_negro.__str__(), '♞1')
        self.assertEqual(self.caballo_blanco.__color__, 'blanco')
        self.assertEqual(self.caballo_negro.__color__, 'negro')

    def test_movimiento_valido(self):
        movimiento_b = self.caballo_blanco.verificar_movimiento(6, 3)
        self.assertEqual(movimiento_b, True)
        self.assertEqual(self.caballo_blanco.movimiento, 'Caballo')
        movimiento_n = self.caballo_negro.verificar_movimiento(3, 3)
        self.assertEqual(movimiento_n, True)
        self.assertEqual(self.caballo_negro.movimiento, 'Caballo')
        
    def test_movimiento_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.caballo_blanco.verificar_movimiento(6, 4)
        self.assertEqual(str(context.exception), 'Movimiento no valido')

if __name__ == '__main__':
    unittest.main()

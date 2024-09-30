import unittest
from Juego.Piezas.torre import Torre

class TestTorre(unittest.TestCase):

    def setUp(self):
        self.torre_negro = Torre('negro', id = 1)
        self.torre_blanco = Torre('blanco', id = 1)

    def test_inicializacion(self):
        self.assertEqual(self.torre_blanco.__str__(), '♖1')
        self.assertEqual(self.torre_negro.__str__(), '♜1')
        self.assertEqual(self.torre_blanco.__color__, 'blanco')
        self.assertEqual(self.torre_negro.__color__, 'negro')

    # Movimiento recto válido
    def test_movimiento_valido(self):
        movimiento_f = self.torre_blanco.verificar_movimiento(8, 3)
        self.assertEqual(movimiento_f, True)
        
        movimiento_c = self.torre_blanco.verificar_movimiento(6, 1)
        self.assertEqual(movimiento_c, True)
    
    # Movimiento inválido que no sea recto
    def test_movimiento_invalido(self):
        self.assertFalse(self.torre_blanco.verificar_movimiento(7, 2))  # Movimiento diagonal

if __name__ == '__main__':
    unittest.main()

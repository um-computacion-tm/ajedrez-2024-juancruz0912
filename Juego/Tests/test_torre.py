import unittest
from Juego.Clases.Piezas.Torre import Torre

class TestTorre(unittest.TestCase):

    def setUp(self):
        self.torre_negro = Torre('negro', 1, 1, 1)
        self.torre_blanco = Torre('blanco', 1, 8, 1)

    def test_inicializacion(self):
        self.assertEqual(self.torre_blanco.__str__(), '♖1')
        self.assertEqual(self.torre_negro.__str__(), '♜1')
        self.assertEqual(self.torre_blanco.__color__, 'blanco')
        self.assertEqual(self.torre_negro.__color__, 'negro')

    # Movimiento recto válido
    def test_movimiento_valido(self):
        movimiento_f = self.torre_blanco.verificar_movimiento(8, 3)
        self.assertEqual(movimiento_f, True)
        self.assertEqual(self.torre_blanco.movimiento, 'Recto')
        
        movimiento_c = self.torre_blanco.verificar_movimiento(6, 1)
        self.assertEqual(movimiento_c, True)
        self.assertEqual(self.torre_blanco.movimiento, 'Recto')
    
    # Movimiento inválido que no sea recto
    def test_movimiento_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.torre_blanco.verificar_movimiento(7, 2)
        self.assertEqual(str(context.exception), 'Movimiento no valido' )  # Movimiento diagonal

if __name__ == '__main__':
    unittest.main()
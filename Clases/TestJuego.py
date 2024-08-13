import unittest
from Juego import Juego

class TestJuego(unittest.TestCase):

    juego = Juego('tablero', 'Alice', 'Bob')

    def test_initialization(self):
        self.juego = Juego('tablero', 'Alice', 'Bob')
        self.assertEqual(self.juego.__estado__, 0)
        self.assertEqual(self.juego.__tablero__, 'tablero')
        self.assertEqual(self.juego.__blanco__, 'Alice')
        self.assertEqual(self.juego.__negro__, 'Bob')
        self.assertEqual(self.juego.__turno__, 'Alice')

    def test_empezar_juego(self):
        self.juego = Juego('tablero', 'Alice', 'Bob')
        self.juego.empezar_juego()
        self.assertEqual(self.juego.__estado__, 1)

    def test_terminar_juego(self):
        self.juego = Juego('tablero', 'Alice', 'Bob')
        self.juego.terminar_juego()
        self.assertEqual(self.juego.__estado__, 0)

if __name__ == '__main__':
    unittest.main()
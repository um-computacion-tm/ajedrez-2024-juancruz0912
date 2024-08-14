import unittest
from Juego import Juego

class TestJuego(unittest.TestCase):

    juego = Juego('Alice', 'Bob')

    def test_iniciar(self):
        self.assertEqual(self.juego.__estado__, 1)
        self.assertEqual(self.juego.__blanco__, 'Alice')
        self.assertEqual(self.juego.__negro__, 'Bob')
        self.assertEqual(self.juego.__turno__, 'Alice')

    def test_empezar_juego(self):
        self.juego.empezar_juego()
        self.assertEqual(self.juego.__estado__, 1)

    def test_terminar_juego(self):
        self.juego.terminar_juego()
        self.assertEqual(self.juego.__estado__, 0)

if __name__ == '__main__':
    unittest.main()
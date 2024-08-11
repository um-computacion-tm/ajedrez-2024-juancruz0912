import unittest
from main import ajedrez

class Testa(unittest.TestCase):
    def testa(self):
        self.assertEqual(ajedrez(), "Juego del Ajedrez")

if __name__ == '__main__':
    unittest.main()
import unittest
from Tablero import Tablero

class TestTablero(unittest.TestCase):

    tablero = Tablero()

    def test_iniciar_tablero(self):
        self.assertEqual(self.tablero.__tablero__[0], [" ", "A", "B", "C", "D", "E", "F", "G", "H"])
        self.assertEqual(self.tablero.__tablero__[1], ["1","T", "C", "A", "Q", "K", "A", "C", "T"])
        self.assertEqual(self.tablero.__tablero__[2], ["2"] + ["P"] * 8)
        self.assertEqual(self.tablero.__tablero__[7], ["7"] + ["P"] * 8)
        self.assertEqual(self.tablero.__tablero__[8], ["8","T", "C", "A", "Q", "K", "A", "C", "T"])
        for i in range(1, 9):
            self.assertEqual(self.tablero.__tablero__[i][0], str(i))


    def test_ver_celda(self):
        self.assertEqual(self.tablero.ver_celda(1,1), 'T')
        self.assertEqual(self.tablero.ver_celda(0,0), 'vacio')    

if __name__ == '__main__':
    unittest.main()
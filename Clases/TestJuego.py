import unittest
from unittest.mock import patch
from Juego import Juego 

class TestJuego(unittest.TestCase):

    juego = Juego('Juan', 'Pedro')

    def test_iniciar(self):
        self.assertEqual(self.juego.__estado__, 1)
        self.assertEqual(self.juego.__blanco__, 'Juan')
        self.assertEqual(self.juego.__negro__, 'Pedro')
        self.assertEqual(self.juego.__turno__, 'Juan')

    def test_cambiar_turno(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__negro__)
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__blanco__)
    
    def test_empezar_juego(self):
        self.juego.empezar_juego()
        self.assertEqual(self.juego.__estado__, True)

    def test_terminar_juego(self):
        self.juego.terminar_juego()
        self.assertEqual(self.juego.__estado__, False)


if __name__ == '__main__':
    unittest.main()
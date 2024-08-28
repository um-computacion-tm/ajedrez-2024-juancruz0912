import unittest
from unittest.mock import patch
from .Juego import Juego 
from .Tablero import Tablero
from .Piezas.Peon import Peon

class TestJuego(unittest.TestCase):

    def setUp(self):
        self.juego = Juego('Juan', 'Pedro')

    # Test para verificar que se inicie de forma correcta la instancia
    def test_iniciar(self):
        self.assertFalse(self.juego.estado)
        self.assertIsInstance(self.juego.tablero, Tablero)
        self.assertEqual(self.juego.__blanco__, "Juan")
        self.assertEqual(self.juego.__negro__, "Pedro")
        self.assertEqual(self.juego.__turno__, "Juan")

    # Test para el metodo empezar_juego
    def test_empezar_juego(self):
        self.juego.empezar_juego()
        self.assertEqual(self.juego.__estado__, True)

    # Test para el metodo terminar_juego
    def test_terminar_juego(self):
        self.juego.terminar_juego()
        self.assertEqual(self.juego.__estado__, False)

    # Test para el metodo cambiar_turno
    def test_cambiar_turno(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__negro__)
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__blanco__)
    
    def test_mover_pieza(self):
        self.juego.empezar_juego()
        self.juego.mover_pieza(5, 'A', 'Peon 1')
        self.assertIsInstance(self.juego.tablero.tablero[5][1], Peon)

    def test_buscar_pieza_existente(self):
        self.juego.empezar_juego()
        existe = self.juego.buscar_pieza('Torre 1')
        self.assertTrue(existe)

    def test_buscar_pieza_no_existente(self):
        self.juego.empezar_juego()
        existe = self.juego.buscar_pieza('Torre X')
        self.assertFalse(existe)

if __name__ == '__main__':

    unittest.main()
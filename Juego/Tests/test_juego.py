import unittest
from Juego.Clases.Juego import Juego 
from Juego.Clases.Tablero import Tablero
from Juego.Clases.Piezas.Peon import Peon

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

    # Test para el método empezar_juego
    def test_empezar_juego(self):
        self.juego.empezar_juego()
        self.assertEqual(self.juego.__estado__, True)

    # Test para el método terminar_juego
    def test_terminar_juego(self):
        self.juego.terminar_juego()
        self.assertEqual(self.juego.__estado__, False)

    # Simula que el tablero indica que solo quedan piezas blancas
    def test_ganar_juego_blanco(self):
        self.juego.tablero.colocar_piezas() 
        piezas_a_remover = [nombre for nombre, pieza in self.juego.tablero.piezas.items() if pieza.color == 'negro']  # Remover todas las piezas negras
        for pieza in piezas_a_remover:
            del self.juego.tablero.piezas[pieza]
        resultado = self.juego.ganar_juego()
        self.assertEqual(resultado, 'Juan es el ganador')

    # Simula que el tablero indica que solo quedan piezas negras
    def test_ganar_juego_negro(self):   
        self.juego.tablero.colocar_piezas() 
        piezas_a_remover = [nombre for nombre, pieza in self.juego.tablero.piezas.items() if pieza.color == 'blanco']  # Remover todas las piezas blancas
        for pieza in piezas_a_remover:
            del self.juego.tablero.piezas[pieza]
        resultado = self.juego.ganar_juego()
        self.assertEqual(resultado, 'Pedro es el ganador')


    # Simula que el tablero indica que aún hay piezas de ambos colores
    def test_ganar_juego_sin_ganador(self):
        self.juego.tablero.colocar_piezas()  # Coloca las piezas en el tablero
        resultado = self.juego.ganar_juego()
        self.assertIsNone(resultado)

    # Test para el método cambiar_turno
    def test_cambiar_turno(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__negro__)
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__blanco__)
    
    def test_mover_pieza(self):
        self.juego.tablero.colocar_piezas()
        self.juego.empezar_juego()
        self.juego.mover_pieza(6, 'A', 'Peon 1')  
        self.assertIsInstance(self.juego.tablero.tablero[6][1], Peon)

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

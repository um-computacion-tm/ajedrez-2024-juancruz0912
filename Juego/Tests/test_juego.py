import unittest
from Juego.juego import Juego 
from unittest.mock import MagicMock
from Juego.tablero import Tablero
from Juego.Piezas.peon import Peon

class TestJuego(unittest.TestCase):

    def setUp(self):
        self.juego = Juego('Juan', 'Pedro')
        self.juego2 = Juego('Jugador Blanco', 'Jugador Negro')
        self.juego2.tablero = MagicMock()
        self.juego2.tablero.jaque_mate_tablero = MagicMock()

    # Test para verificar que se inicie de forma correcta la instancia
    def test_iniciar(self):
        self.assertTrue(self.juego.estado)
        self.assertIsInstance(self.juego.tablero, Tablero)
        self.assertEqual(self.juego.__blanco__, "Juan")
        self.assertEqual(self.juego.__negro__, "Pedro")
        self.assertEqual(self.juego.__turno__, "Juan")


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
        resultado = self.juego.ganar_juego('negro')
        self.assertEqual(resultado, 'Juan es el ganador')

    # Simula que el tablero indica que solo quedan piezas negras
    def test_ganar_juego_negro(self):   
        self.juego.tablero.colocar_piezas() 
        piezas_a_remover = [nombre for nombre, pieza in self.juego.tablero.piezas.items() if pieza.color == 'blanco']  # Remover todas las piezas blancas
        for pieza in piezas_a_remover:
            del self.juego.tablero.piezas[pieza]
        resultado = self.juego.ganar_juego('negro')
        self.assertEqual(resultado, 'Pedro es el ganador')


    # Simula que el tablero indica que aún hay piezas de ambos colores
    def test_ganar_juego_sin_ganador(self):
        self.juego.tablero.colocar_piezas()  # Coloca las piezas en el tablero
        resultado = self.juego.ganar_juego('negro')
        self.assertIsNone(resultado)

    # Test para el método cambiar_turno
    def test_cambiar_turno(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__negro__)
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.__turno__, self.juego.__blanco__)

    def test_pieza_no_existe(self):
        with self.assertRaises(ValueError) as context:
            self.juego.existe_pieza('Peon 90') 
        
    def test_mover_pieza(self):
        self.juego.tablero.colocar_piezas()
        self.juego.mover_pieza(6, 'A', 'Peon 1 blanco')  
        self.assertIsInstance(self.juego.tablero.tablero[6][1], Peon)

    def test_buscar_pieza_no_existente(self):
        with self.assertRaises(ValueError) as context:
            self.juego.existe_pieza('Torre X')
        self.assertIn(str(context.exception), 'Torre X no existe')

    def test_buscar_pieza_existente(self):
        self.assertEqual(str(self.juego.existe_pieza('Peon 1'),), 'Peon 1 blanco')

    def test_verificar_fila_correcta(self):
        self.assertCountEqual(str(self.juego.verificar_fila(3)), '3')
    
    def test_verificar_fila_incorrecta(self):
        with self.assertRaises(ValueError) as context:
            self.juego.verificar_fila(9)
        self.assertIn(str(context.exception), 'La fila 9 no existe' )


if __name__ == '__main__':
    unittest.main()

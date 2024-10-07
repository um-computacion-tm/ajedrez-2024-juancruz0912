import unittest
from Juego.juego import Juego 
from unittest.mock import MagicMock
from Juego.tablero import Tablero

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


    # Se simula que el rey blanco está en jaque mate
    def test_ganar_juego_jaque_mate(self):
        self.juego2.quedan_reyes = MagicMock(return_value=None) # Simula que el tablero tiene reyes de ambos colores
        self.juego2.__tablero__.jaque_mate_tablero.return_value = True # Simula que el rey blanco está en jaque mate
        resultado = self.juego2.ganar_juego('blanco')
        self.assertEqual(resultado, '---  El rey blanco esta en jaque mate, por lo tanto Jugador Negro es el ganador!! ---')


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
        self.assertEqual(self.juego.mover_pieza(6, 'A', 'Peon 1 blanco'), None)  

    def test_mover_pieza_invalida(self):
        self.juego.tablero.colocar_piezas()
        with self.assertRaises(ValueError) as context:
            self.juego.mover_pieza(4, 'A', 'Peon 1 blanco')  
        self.assertEqual(str(context.exception), 'Movimiento no valido')

    def test_buscar_pieza_no_existente(self):
        with self.assertRaises(ValueError) as context:
            self.juego.existe_pieza('Torre X')
        self.assertIn(str(context.exception), 'Torre X no existe')

    def test_buscar_pieza_existente(self):
        self.assertEqual(str(self.juego.existe_pieza('Peon 1'),), 'Peon 1 blanco')

    def test_verificar_fila_correcta(self):
        self.assertTrue(self.juego.verificar_fila(3))
    
    def test_verificar_fila_incorrecta(self):
        self.assertFalse(self.juego.verificar_fila(9))

    def test_verificar_columna_correcta(self):
        self.assertTrue(self.juego.verificar_columna('A'))
    
    def test_verificar_columna_incorrecta(self):
        self.assertFalse(self.juego.verificar_columna('Z'))

    def test_verificar_entrada_correcta(self):
        self.assertTrue(self.juego.verificar_entrada(3, 'A'))


if __name__ == '__main__':
    unittest.main()

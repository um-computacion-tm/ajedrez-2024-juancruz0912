import unittest
from unittest.mock import patch, MagicMock
from Juego.juego import Juego 
from Juego.main import main, jugar

class TestJuegoAjedrez(unittest.TestCase):

    def setUp(self):
        self.juego = Juego("Jugador1", "Jugador2")

    @patch('builtins.input', return_value='0')
    def test_jugar_terminar_juego(self, mock_input):
        self.juego.terminar_juego = MagicMock()
        jugar(self.juego)
        self.juego.terminar_juego.assert_called_once()


    @patch('builtins.input', side_effect=['Jugador1', 'Jugador2', '0'])
    def test_main_terminar_juego(self, mock_input):
        self.juego.empezar_juego = MagicMock()
        self.juego.terminar_juego = MagicMock()

        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call('Se termino el juego')

    
if __name__ == '__main__':
    unittest.main()

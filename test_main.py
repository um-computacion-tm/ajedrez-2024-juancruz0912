import unittest
from unittest.mock import patch, MagicMock
from Clases.Juego import Juego
from main import main, jugar, mover, mover_pieza_valida

class TestJuegoAjedrez(unittest.TestCase):

    def setUp(self):
        self.juego = Juego("Jugador1", "Jugador2")

    @patch('builtins.input', return_value='0')
    def test_jugar_terminar_juego(self, mock_input):
        self.juego.terminar_juego = MagicMock()
        jugar(self.juego)
        self.juego.terminar_juego.assert_called_once()

    @patch('builtins.input', side_effect=['3', 'B'])
    def test_mover_pieza_valida(self, mock_input):
        self.juego.buscar_pieza = MagicMock(return_value=True)
        self.juego.mover_pieza = MagicMock()
        self.juego.cambiar_turno = MagicMock()

        mover_pieza_valida(self.juego, 'Torre1')

        self.juego.mover_pieza.assert_called_once_with(3, 'B', 'Torre1')
        self.juego.cambiar_turno.assert_called_once()

    @patch('builtins.input', side_effect=['invalid', '1', 'B'])
    @patch('Clases.Juego.Juego.mover_pieza')
    def test_mover_pieza_valida_movimiento_invalido(self, mock_mover_pieza, mock_input):
        mock_mover_pieza.side_effect = ValueError('Movimiento inválido')
        with self.assertRaises(ValueError):
            mover_pieza_valida(self.juego, 'Torre1')
        
        self.assertEqual(mock_input.call_count, 1) # Chequear que se haya llamado a input una vez
        self.assertEqual(mock_mover_pieza.call_count, 0)

    @patch('builtins.input', side_effect=['Torre1', '0'])
    def test_mover_pieza_invalida(self, mock_input):
        self.juego.buscar_pieza = MagicMock(return_value=False)

        with patch('builtins.print') as mock_print:
            mover(self.juego)
            mock_print.assert_called_with('Torre1 no existe')

    @patch('builtins.input', side_effect=['Torre1', '3', 'B'])
    def test_mover_pieza_valida(self, mock_input):
        self.juego.buscar_pieza = MagicMock(return_value=True)
        self.juego.mover_pieza = MagicMock()
        self.juego.cambiar_turno = MagicMock()

        mover(self.juego)

        self.juego.mover_pieza.assert_called_once_with(3, 'B', 'Torre1')
        self.juego.cambiar_turno.assert_called_once()

    @patch('builtins.input', side_effect=['Jugador1', 'Jugador2', '0'])
    def test_main_terminar_juego(self, mock_input):
        self.juego.empezar_juego = MagicMock()
        self.juego.terminar_juego = MagicMock()

        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call('Se termino el juego')

if __name__ == '__main__':
    unittest.main()

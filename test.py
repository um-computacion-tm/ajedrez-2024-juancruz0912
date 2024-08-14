import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['Alice', 'Bob'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        
        main()
        output = mock_stdout.getvalue().strip().split('\n')

        self.assertIn('Bienvenidos al juego del ajedrez', output)
        self.assertIn('Ingresar los nombres de los jugadores', output)
        self.assertIn('blancas : Alice negras: Bob', output)

if __name__ == '__main__':
    unittest.main()

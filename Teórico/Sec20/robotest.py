import unittest
from robo import Robo

class RoboTeste(unittest.TestCase):
    def setUp(self):
        self.megaman = Robo('MegaMan', bateria=50)
        print('setUp executado')

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria,100)

    def test_dizer_nome (self):
        self.assertEqual(self.megaman.diz_nome(), 'BEEP BOOP BEEP BOOP EU SO O MEGAMAN')
        self.assertEqual(self.megaman.bateria , 49, 'A bateria tem que estar em 49')

    def tearDown(self):
        print('tearDown() executado ')


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    unittest.main()

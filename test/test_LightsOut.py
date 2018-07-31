import unittest

from LightsOut import LightsOut


class MyTestCase(unittest.TestCase):
    def test_3x4(self):
        board = '\n'.join(['....', '.O..', '....'])
        lightsout = LightsOut(3, 4, board)
        num = lightsout.solve()
        self.assertEqual(num, 4)  # 4回で解ける

    def test_4x5(self):
        board = '\n'.join(['.....', '.O...', '.....', '.....'])
        lightsout = LightsOut(4, 5, board)
        num = lightsout.solve()
        self.assertEqual(num, 9)  # 9回で解ける


if __name__ == '__main__':
    unittest.main()

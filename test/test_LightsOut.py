import unittest
import time
import inspect
from LightsOut import LightsOut


class MyTestCase(unittest.TestCase):
    def test_solve_round_robin_3x4(self):
        board = '\n'.join(['....', '.O..', '....'])
        lightsout = LightsOut(board)
        start = time.time()
        num = lightsout.solve_round_robin()
        print('elapsed ' + inspect.stack()[0][3] + ': ', time.time() - start)
        self.assertEqual(num, 4)  # 4回で解ける

    def test_solve_round_robin_4x5(self):
        board = '\n'.join(['.....', '.O...', '.....', '.....'])
        lightsout = LightsOut(board)
        start = time.time()
        num = lightsout.solve_round_robin()
        print('elapsed ' + inspect.stack()[0][3] + ': ', time.time() - start)
        self.assertEqual(num, 9)  # 9回で解ける

    def test_solve_first_row_combinations_3x4(self):
        board = '\n'.join(['....', '.O..', '....'])
        lightsout = LightsOut(board)
        start = time.time()
        num = lightsout.solve_first_row_combinations()
        print('elapsed ' + inspect.stack()[0][3] + ': ', time.time() - start)
        self.assertEqual(num, 4)  # 4回で解ける

    def test_solve_first_row_combinations_4x5(self):
        board = '\n'.join(['.....', '.O...', '.....', '.....'])
        lightsout = LightsOut(board)
        start = time.time()
        num = lightsout.solve_first_row_combinations()
        print('elapsed ' + inspect.stack()[0][3] + ': ', time.time() - start)
        self.assertEqual(num, 9)  # 9回で解ける


if __name__ == '__main__':
    unittest.main()

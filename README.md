Lights Out Solver
====

[Lights Out](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%82%A4%E3%83%84%E3%82%A2%E3%82%A6%E3%83%88) を解くプログラムです。

実装状況
- 総当たり
- 1行目は総当たり、２行目以降はライトONの下のセルを押す

## Requirement

Python3

## Usage

```python
from LightsOut import LightsOut

board = '\n'.join(
    ['.....',
     '.O...',
     '.....',
     '.....'])
lightsout = LightsOut(board)
num = lightsout.solve_round_robin()  # 9
num = lightsout.solve_first_row_combinations()  # 9
```

### Test
```bash
$ python3 -m unittest discover -s test
elapsed test_solve_first_row_combinations_3x4:  0.012784242630004883
.elapsed test_solve_first_row_combinations_4x5:  0.0010991096496582031
.elapsed test_solve_round_robin_3x4:  0.01643085479736328
.elapsed test_solve_round_robin_4x5:  11.505574941635132
.
----------------------------------------------------------------------
Ran 4 tests in 11.537s

OK
```

## Licence

MIT

## Author

[kangaechu](https://github.com/kangaechu)

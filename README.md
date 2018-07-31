Lights Out Solver
====

[Lights Out](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%82%A4%E3%83%84%E3%82%A2%E3%82%A6%E3%83%88) を解くプログラムです。
現在は総当たりだけ実装。

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
lightsout = LightsOut(4, 5, board)
num = lightsout.solve()  # 9
```

## Licence

MIT

## Author

[kangaechu](https://github.com/kangaechu)

import copy
import itertools


class LightsOut:
    """
    Lights Out
    https://ja.wikipedia.org/wiki/ライツアウト
    O = オン . = オフ
    """

    def __init__(self, my_board: str):
        self.board = self.parse_board(my_board)
        self.width = len(self.board[0])
        self.height = len(self.board)

    def __str__(self):
        return self.to_str()

    @staticmethod
    def parse_board(board_str):
        """
        テキスト形式のboardをTrue/Falseのリストに変換
        :param board_str:
        :return:
        """
        out_board = []
        for row in board_str.split('\n'):
            out_row = []
            for cell in row:
                if cell == 'O':
                    out_row.append(True)
                elif cell == '.':
                    out_row.append(False)
                else:
                    raise KeyError
            out_board.append(out_row)
        return out_board

    def to_str(self):
        """
        boardをテキスト形式に変換
        :return:
        """
        out_str = ''
        for row in self.board:
            for cell in row:
                if cell:
                    out_str += 'O'
                else:
                    out_str += '.'
            out_str += '\n'
        return out_str

    @staticmethod
    def __is_all_off(my_board):
        """
        すべて消灯しているか
        :return:
        """
        return not any([any(row) for row in my_board])

    def __push(self, row: int, column: int, board: list):
        """
        ある行列のボタンを押す
        ボタンの位置と上下左右の位置も反転される
        :param row: 押したボタンの行番号(1 - width)
        :param column: 押したボタンの列番号(1- height)
        :param board:  ボード
        :return:
        """
        r = row
        c = column

        board[r][c] = not board[r][c]

        # 左のセル
        if c - 1 >= 0:
            board[r][c - 1] = not board[r][c - 1]
        # 右のセル
        if c + 1 <= self.width - 1:
            board[r][c + 1] = not board[r][c + 1]
        # 下のセル
        if r + 1 <= self.height - 1:
            board[r + 1][c] = not board[r + 1][c]
        # 上のセル
        if r - 1 >= 0:
            board[r - 1][c] = not board[r - 1][c]
        return board

    def push(self, row: int, column: int):

        self.board = self.__push(row, column, self.board)

    def solve_round_robin(self):
        """
        総当たりによる最適手法検索
        :return:
        """
        wh = [[w, h] for w in range(self.height) for h in range(self.width)]
        for i in range(1, len(wh)):
            for combinations in itertools.combinations(wh, i):
                temp_board = copy.deepcopy(self.board)
                for c in combinations:
                    temp_board = self.__push(c[0], c[1], temp_board)
                if self.__is_all_off(temp_board):
                    return len(combinations)
        return -1


if __name__ == '__main__':
    board = '\n'.join(['....', '.O..', '....'])
    lightsout = LightsOut(3, 4, board)
    print(lightsout)
    print(lightsout.solve_round_robin())

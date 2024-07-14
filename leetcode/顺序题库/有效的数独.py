from typing import List

from self import self


def isValidSudoku(self, board: List[List[str]]) -> bool:
    # 判断每行每列是否合法
    def check_row_col(i: int, j: int) -> bool:
        for i in range(9):
            s_row = set()
            s_col = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in s_row:
                        return False
                    else:
                        s_row.add(board[i][j])
                if board[j][i].isdigit():
                    if board[j][i] in s_col:
                        return False
                    else:
                        s_col.add(board[j][i])
        return True

    if not check_row_col(0, 0):
        return False

    # 判断每3*3矩阵内是否合法
    def check_per(i: int, j: int) -> bool:
        s = set()
        for m in range(i, i + 3):
            for n in range(j, j + 3):
                if board[m][n].isdigit():
                    if board[m][n] in s:
                        return False
                    else:
                        s.add(board[m][n])
        return True

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not check_per(i, j):
                return False
    return True


board = [[".", ".", ".", ".", ".", ".", "5", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", "3", ".", ".", "2", ".", "4", ".", "."],
         [".", ".", "7", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "3", "4", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "."],
         [".", ".", ".", ".", ".", "5", "2", ".", "."]]

print(isValidSudoku(self, board))

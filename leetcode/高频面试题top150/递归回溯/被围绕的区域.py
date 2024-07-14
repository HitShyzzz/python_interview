from typing import List

from self import self


def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    '''
    判断那些O被X包围很难，于是我们判断那些O不被X包围，
    也就是只要O直接或者间接与边界上的O相连，那么这些O就一定不被X包围
    '''

    def dfs(i: int, j: int):
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] == 'X' or board[i][j] == 'A':
            return
        board[i][j] = 'A'
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    for i in range(len(board)):
        dfs(i, 0)
        dfs(i, len(board[0]) - 1)
    for j in range(len(board[0])):
        dfs(0, j)
        dfs(len(board) - 1, j)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'A':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
solve(self, board)
print(board)

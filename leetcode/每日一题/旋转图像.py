from typing import List

from self import self


# 使用辅助矩阵
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    matrix_new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 原矩阵的[i,j]出现在新矩阵的倒数第i列第j个位置
            matrix_new[j][n - 1 - i] = matrix[i][j]
    # 再赋值给原矩阵
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix_new[i][j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(self, matrix)
print(matrix)

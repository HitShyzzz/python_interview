from typing import List

from self import self

'''
不使用辅助矩阵
关键点还是matrix[i][j]旋转到了倒数第i行第j个位置
matrix[i][j]=matrix[j][n-1-i] → matrix[n-1-j][i]=matrix[i][j]
当n为偶数时，需要枚举n^2/4=n/2*(n/2)个位置
当n为奇数时，需要枚举(n^2-1)/2=(n-1)/2*(n+1)/2个位置，最中心的元素无须旋转
'''


def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(self, matrix)
print(matrix)

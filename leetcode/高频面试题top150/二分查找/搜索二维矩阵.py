from typing import List

from self import self


# 对每一行进行二分查找
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        if matrix[i][0] == target or matrix[i][n - 1] == target:
            return True
        elif matrix[i][0] < target < matrix[i][n - 1]:
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
    return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20
print(searchMatrix(self, matrix, target))

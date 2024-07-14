from typing import List

from self import self


def longestIncreasingPath(self, matrix: [List[int]]) -> int:
    import functools
    @functools.lru_cache(None)
    def dfs(i: int, j: int) -> int:
        if i < 0 or i == len(matrix) or j < 0 or j == len(matrix[0]):
            return 0
        cur = matrix[i][j]
        res = 1
        if i - 1 >= 0 and cur > matrix[i - 1][j]:
            res = max(res, dfs(i - 1, j) + 1)

        if i + 1 < len(matrix) and cur > matrix[i + 1][j]:
            res = max(res, dfs(i + 1, j) + 1)

        if j - 1 >= 0 and cur > matrix[i][j - 1]:
            res = max(res, dfs(i, j - 1) + 1)

        if j + 1 < len(matrix[0]) and cur > matrix[i][j + 1]:
            res = max(res, dfs(i, j + 1) + 1)

        return res

    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ans = max(ans, dfs(i, j))
    return ans


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

print(longestIncreasingPath(self, matrix))

from typing import List

from self import self


# 输入：grid = [[0,0,1],[1,0,1],[0,0,0]]
# 输出：1
def findChampion(self, grid: List[List[int]]) -> int:
    n = len(grid)
    for i, line in enumerate(grid):
        if sum(line) == n - 1:
            return i


grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
print(findChampion(self, grid))

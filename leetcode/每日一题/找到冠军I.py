from typing import List

from self import self


# 输入：grid = [[0,0,1],[1,0,1],[0,0,0]]
# 输出：1
def findChampion(self, grid: List[List[int]]) -> int:
    for i in range(len(grid)):
        cnt = 0
        for j in range(len(grid[0])):
            if i != j and grid[i][j] == 1:
                cnt = cnt + 1
            if cnt == len(grid[0]) - 1:
                return i
    return 0


grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
print(findChampion(self, grid))

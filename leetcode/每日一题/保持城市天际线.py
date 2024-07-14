from typing import List
import numpy as np
from self import self


# 输入：grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# 输出：35
# 解释：建筑物的高度如上图中心所示。
# 用红色绘制从不同方向观看得到的天际线。
# 在不影响天际线的情况下，增加建筑物的高度：
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]
def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    # 每行的最大值
    row_max = np.max(grid, axis=1)
    # 每列的最大值
    col_max = np.max(grid, axis=0)
    max_increase = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_increase += min(row_max[i], col_max[j]) - grid[i][j]
    return max_increase


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(maxIncreaseKeepingSkyline(self, grid))

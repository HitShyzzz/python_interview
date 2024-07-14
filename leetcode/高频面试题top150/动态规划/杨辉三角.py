from typing import List

from self import self


# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
def generate(self, numRows: int) -> List[List[int]]:
    ans = []
    for i in range(numRows):
        row = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])
        ans.append(row)
    return ans


print(generate(self, 5))

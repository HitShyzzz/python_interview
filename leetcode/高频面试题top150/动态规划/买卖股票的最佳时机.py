from typing import List

from self import self


# 输入：[7,1,5,3,6,4]
# 输出：5
def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    a = prices[n - 1]
    ans = 0
    for i in range(n - 2, -1, -1):
        a = max(prices[i], a)
        ans = max(ans, a - prices[i])
    return ans


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(self, prices))

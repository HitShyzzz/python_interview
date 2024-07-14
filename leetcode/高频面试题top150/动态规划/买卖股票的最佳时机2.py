from typing import List

from self import self


def maxProfit(self, prices: List[int]) -> int:
    a = 0
    b = -prices[0]
    for i in range(1, len(prices)):
        prev_a = a
        prev_b = b
        a = max(prev_b + prices[i], prev_a)
        b = max(prev_a - prices[i], prev_b)
    return a


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(self, prices))

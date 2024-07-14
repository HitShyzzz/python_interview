from typing import List

from self import self


# coins=[1,2,3,5]
# amount=14
# 输出4
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [100001] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == 100001 else dp[amount]

coins = [1, 2, 5]
amount = 11
print(coinChange(self, coins, amount))

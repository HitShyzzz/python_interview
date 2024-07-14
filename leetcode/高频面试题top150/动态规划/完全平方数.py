import functools
import math

from self import self


@functools.lru_cache(None)
def numSquares(self, n: int) -> int:
    dp = [n] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(int(math.sqrt(i)), 0, -1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp[n]


print(numSquares(self, 12))

from typing import List

from self import self


def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    dp = [True] + [False] * (n - 1)
    for i in range(1, n):
        for j in range(0, i):
            if j + nums[j] >= i:
                dp[i] = dp[i] | dp[j]
                if dp[i]:
                    break
    return dp[n - 1]


nums = [3, 2, 1, 0, 4]
print(canJump(self, nums))

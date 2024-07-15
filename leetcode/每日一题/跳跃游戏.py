from typing import List

from self import self

'''
O(T)=O(N^2) 会超时
'''
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    # dp[i]表示能否到达下标i的位置
    dp = [False] * n
    dp[0] = True
    for i in range(1, n):
        for j in range(0, i):
            if i - j <= nums[j]:
                dp[i] = dp[j]
                if dp[i]:
                    break
    return dp[n - 1]


nums = [2, 3, 1, 1, 4]
print(canJump(self, nums))

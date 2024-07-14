from typing import List

from self import self


def countSmaller(self, nums: List[int]) -> List[int]:
    n = len(nums)
    dp = [0] * n
    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            dp[i] = dp[i + 1] + 1
        elif nums[i] == nums[i + 1]:
            dp[i] = dp[i + 1]
        else:
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    dp[i] = dp[j] + 1
                    break
                elif nums[i] == nums[j]:
                    dp[i] = dp[j]
                    break
    return dp


nums = [2, 0, 1]
print(countSmaller(self, nums))

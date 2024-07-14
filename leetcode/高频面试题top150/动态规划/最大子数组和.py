from typing import List

from self import self


# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# dp[i]表示以nums[i]结尾的最大连续子数组之和！
def maxSubArray(self, nums: List[int]) -> int:
    ans = nums[0]
    a = 0
    for num in nums:
        a = max(a + num, num)
        ans = max(ans, a)
    return ans


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(self, nums))

from typing import List

from self import self

'''
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
'''


def maxSubArray(self, nums: List[int]) -> int:
    sum = 0
    max_sum = nums[0]
    for num in nums:
        if sum < 0:
            sum = num
        else:
            sum += num
        max_sum = max(max_sum, sum)
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(self, nums))

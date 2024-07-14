from typing import List

from self import self


# 输入：nums = [-2,-1,-1,1,2,3]
# 输出：3
# 解释：共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
def maximumCount(self, nums: List[int]) -> int:
    n = len(nums)
    neg = 0
    zero = 0
    for i in range(n):
        if nums[i] < 0:
            neg = neg + 1
        elif nums[i] == 0:
            zero = zero + 1
        else:
            break
    return max(neg, n - neg - zero)


nums = [-2, -1, -1, 1, 2, 3]
print(maximumCount(self, nums))

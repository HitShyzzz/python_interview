from typing import List

from self import self


# nums=[2,3,-2,4]
# 输出 40
def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    max_proc = nums[0]
    min_proc = nums[0]
    ans = nums[0]
    for i in range(1, n):
        prev_max = max_proc
        prev_min = min_proc
        max_proc = max(max(prev_max * nums[i], prev_min * nums[i]), nums[i])
        min_proc = min(min(prev_max * nums[i], prev_min * nums[i]), nums[i])
        ans = max(max_proc, ans)
    return ans


nums = [7, -2, -4]
print(maxProduct(self, nums))

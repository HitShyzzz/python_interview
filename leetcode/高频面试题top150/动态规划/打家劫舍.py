from typing import List

from self import self


# 输入：[2,7,9,3,1]
# 输出：12
def rob(self, nums: List[int]) -> int:
    ans = nums[0]
    cur_steal = nums[0]
    cur_unsteal = 0
    for i in range(1, len(nums)):
        prev_steal = cur_steal
        prev_unsteal = cur_unsteal
        cur_steal = prev_unsteal + nums[i]
        cur_unsteal = max(prev_steal, prev_unsteal)
        ans = max(ans, max(cur_unsteal, cur_steal))
    return ans


nums = [1, 2, 3, 1]
print(rob(self, nums))

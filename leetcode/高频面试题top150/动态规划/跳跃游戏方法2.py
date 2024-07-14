from typing import List

from self import self


def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    max_pos = 0
    for i in range(0, n):
        if max_pos >= n - 1:
            return True
        # 只要当前位置在最远可达位置内，就可以去更新最远可达位置！
        if i <= max_pos:
            max_pos = max(max_pos, i + nums[i])
        else:
            return False


nums = [1, 0, 1, 0]
print(canJump(self, nums))

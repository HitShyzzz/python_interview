import random
from typing import List

from self import self


def findPeakElement(self, nums: List[int]) -> int:
    n = len(nums)
    idx = random.randint(0, n - 1)

    # 获得下标i的元素，主要为了处理边界条件
    def get(i: int) -> int:
        if i == -1 or i == n:
            return float('-inf')
        return nums[i]

    while not (get(idx - 1) < get(idx) and get(idx) > get(idx + 1)):
        # idx+1值大，就往idx+1方向走
        if get(idx) < get(idx + 1):
            idx += 1
        # idx-1值大，就往idx-1方向走
        elif get(idx) < get(idx - 1):
            idx -= 1
    return idx


nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(self, nums))

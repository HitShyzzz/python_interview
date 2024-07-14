from typing import List

from self import self


def findPeakElement(self, nums: List[int]) -> int:
    # 最大元素一定是一个峰值
    return nums.index(max(nums))


nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(self, nums))

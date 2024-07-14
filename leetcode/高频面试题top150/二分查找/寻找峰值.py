from typing import List

from self import self


def findPeakElement(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    if n == 2:
        return 0 if nums[0] > nums[1] else 1
    for i in range(n - 3 + 1):
        if nums[i + 1] > nums[i] and nums[i + 1] > nums[i + 2]:
            return i + 1
    return 0 if nums[0] > nums[n - 1] else n - 1


nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(self, nums))

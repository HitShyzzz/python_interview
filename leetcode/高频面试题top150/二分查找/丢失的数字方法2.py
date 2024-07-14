from typing import List

from self import self


def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(self, nums))

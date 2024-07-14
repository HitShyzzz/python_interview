from typing import List

from self import self


def missingNumber(self, nums: List[int]) -> int:
    ans = 0
    # enumerate()函数用于同时列出列表元素的下标和对应值
    for i, num in enumerate(nums):
        ans ^= i ^ num
    return ans ^ len(nums)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(self, nums))

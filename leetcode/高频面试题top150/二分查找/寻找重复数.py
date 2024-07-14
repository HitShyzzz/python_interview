from collections import Counter
from typing import List

from self import self


def findDuplicate(self, nums: List[int]) -> int:
    return next(item for item, cnt in Counter(nums).items() if cnt > 1)


nums = [1, 3, 4, 2, 2]
arr = Counter(nums)
print(arr)
print(findDuplicate(self, nums))

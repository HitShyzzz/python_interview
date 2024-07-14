from collections import Counter
from typing import List

from self import self

# 利用hash set来判断，O(S)=O(n)
def findDuplicate(self, nums: List[int]) -> int:
    s = set()
    for num in nums:
        if num in s:
            return num
        s.add(num)


nums = [1, 3, 4, 2, 2]
arr = Counter(nums)
print(arr)
print(findDuplicate(self, nums))

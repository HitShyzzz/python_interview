from collections import Counter
from typing import List

from self import self


# 快慢指针
def findDuplicate(self, nums: List[int]) -> int:
    slow = 0
    fast = 0
    while True:
        # 1.慢指针每次走1步
        slow = nums[slow]
        # 2.快指针每次走2步
        fast = nums[nums[fast]]
        # 3.直到快慢指针相遇
        if slow == fast:
            break
    # 4、慢指针重新放到起点
    slow = 0
    while slow != fast:
        # 5、慢指针每次走1步
        slow = nums[slow]
        # 6、快指针每次也走1步
        fast = nums[fast]
    # 7、快慢指针再次相遇就是入环点
    return slow


nums = [1, 3, 4, 2, 2]
arr = Counter(nums)
print(arr)
print(findDuplicate(self, nums))

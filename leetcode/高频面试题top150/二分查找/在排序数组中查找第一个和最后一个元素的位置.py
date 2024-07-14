from typing import List

from self import self
from tqdm import tqdm, trange


def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    start = -1
    end = -1
    l = 0
    r = len(nums) - 1
    # 1、二分查找等于target的起始下标
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            start = mid
            # 找到等于target的元素就继续向左走找起始下标
            r = mid - 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    l = start
    r = len(nums) - 1
    # 2、二分查找等于target的终止下标
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            end = mid
            # 找到等于target的元素就继续向右走找终止下标
            l = mid + 1
        else:
            r = mid - 1
    return [start, end]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(self, nums, target))

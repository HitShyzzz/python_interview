from typing import List

from self import self

def search(self, nums: List[int], target: int) -> int:
    # 1、找到旋转点
    pos = 0
    for i in range(len(nums)):
        if i + 1 < len(nums) and nums[i] > nums[i + 1]:
            pos = i
            break
    l = 0
    r = pos
    # 2、在旋转点左侧[0,pos]二分查找
    while l <= r:
        if target < nums[0]:
            break
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    l = pos + 1
    r = len(nums) - 1
    # 3、在旋转点右侧[pos+1,n-1]二分查找
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 4
print(search(self, nums, target))

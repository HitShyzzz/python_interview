from typing import List

from self import self


def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 求nums1相对于nums2的差集
    intersec = set(nums1).intersection(set(nums2))
    if not intersec:
        return [0, 0]
    cnt1 = 0
    cnt2 = 0
    for i in nums1:
        if i in intersec:
            cnt1 += 1
    for i in nums2:
        if i in intersec:
            cnt2 += 1
    return [cnt1, cnt2]


nums1 = [2, 3, 2]
nums2 = [1, 2]
print(findIntersectionValues(self, nums1, nums2))

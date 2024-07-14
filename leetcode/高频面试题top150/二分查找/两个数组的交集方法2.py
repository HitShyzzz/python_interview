import collections
from typing import List

from self import self


# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    cnt1 = collections.Counter(nums1)
    cnt2 = collections.Counter(nums2)
    cnt = cnt1 & cnt2
    return list(cnt.elements())


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(self, nums1, nums2))

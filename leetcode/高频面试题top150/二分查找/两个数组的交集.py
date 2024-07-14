import collections
from typing import List

from self import self


# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    cnt1 = collections.Counter(nums1)
    cnt2 = collections.Counter(nums2)
    ans = []
    for e, c in cnt1.items():
        if e in cnt2:
            i = 0
            while i < min(c, cnt2[e]):
                ans.append(e)
                i += 1
    return ans


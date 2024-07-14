from typing import List

from self import self


# 输入：nums = [5,4,8,7,10,2]
# 输出：13
def minimumSum(self, nums: List[int]) -> int:
    n = len(nums)
    l = [51] * n
    r = [51] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[j] < nums[i]:
                l[i] = min(l[i], nums[j])
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[j] < nums[i]:
                r[i] = min(r[i], nums[j])
    ans = 153
    for i in range(0, n):
        if l[i] != 51 and r[i] != 51:
            ans = min(ans, l[i] + nums[i] + r[i])
    return ans if ans != 153 else -1


nums = [5, 4, 8, 7, 10, 2]
print(minimumSum(self, nums))

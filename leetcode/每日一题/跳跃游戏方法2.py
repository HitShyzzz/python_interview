from typing import List

from self import self

'''
O(T)=O(N)
'''


def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    # 记录能到达的最远下标
    max_pos = 0
    for i in range(n):
        if max_pos >= n - 1:
            return True
        # 如果当前下标i在max_pos之内，就去更新max_pos
        if i <= max_pos:
            max_pos = max(max_pos, i + nums[i])
        # 此时下标i是不可达的，直接返回False
        else:
            return False


nums = [2, 3, 1, 1, 4]
print(canJump(self, nums))

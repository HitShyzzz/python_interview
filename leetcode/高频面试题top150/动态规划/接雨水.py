from typing import List

from self import self


def trap(self, height: List[int]) -> int:
    n = len(height)
    ans = 0
    left_max = [height[0]] + [0] * (n - 1)
    right_max = [0] * (n - 1) + [height[n - 1]]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    # 对于第i个柱子，能接到的雨水量=左右两侧最高柱子高度的较小者-height[i]
    for i in range(0, n):
        sum = min(left_max[i], right_max[i]) - height[i]
        ans += sum
    return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = trap(self, height)
print(ans)
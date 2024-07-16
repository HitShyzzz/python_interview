from typing import List

from self import self

'''
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
    list1 = nums

    def recur(index: int):
        if index == len(nums):
            ans.append(list(list1))
            return
        for i in range(index, len(nums)):
            # 一一交换两个位置上的元素达到全排列的目的
            swap(index, i, list1)
            recur(index + 1)
            # 回溯
            swap(index, i, list1)

    def swap(i: int, j: int, arrs: List[int]):
        tmp = arrs[i]
        arrs[i] = arrs[j]
        arrs[j] = tmp

    recur(0)
    return ans


nums = [1, 2, 3]
print(permute(self, nums))

from typing import List

from self import self

'''
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
'''


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []

    def recur(index: int, target: int, list: List[int]):
        if target < 0 or index == len(candidates):
            return
        if target == 0:
            ans.append(list[:])
            return
        for i in range(index, len(candidates)):
            list.append(candidates[i])
            # 这里的关键是这个recur(i,target-candidates[i],list)的i，下一个index取i就保证了
            # 每个元素既可以重复取，又可以保证不往前取数
            recur(i, target - candidates[i], list)
            del list[len(list) - 1]

    recur(0, target, [])
    return ans


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(self, candidates, target))

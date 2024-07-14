from typing import List

from self import self


# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # 按start从小到大排序,直接在原矩阵修改
    intervals.sort(key=lambda x: x[0])
    merge_list = []
    for interval in intervals:
        start = interval[0]
        end = interval[1]
        # 不重叠
        if not merge_list or start > merge_list[len(merge_list) - 1][1]:
            merge_list.append(interval)
        else:  # 重叠
            merge_list[len(merge_list) - 1][1] = max(merge_list[len(merge_list) - 1][1], end)
    return merge_list


intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]
print(merge(self, intervals))

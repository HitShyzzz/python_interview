from typing import List

from self import self


def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    l = matrix[0][0]
    r = matrix[n - 1][n - 1]

    # 统计矩阵中小于等于mid元素的个数，一定在mid的左上角
    def check(mid: int) -> int:
        i = n - 1
        j = 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                cnt += (i + 1)
                j += 1
            else:
                i -= 1
        return cnt

    while l < r:
        # [l,mid]和[mid+1,r]
        mid = (l + r) // 2
        cnt = check(mid)
        # cnt>=k，则ans<=cnt,在区间[l,mid]查找
        if cnt >= k:
            r = mid
        # 否则在[mid+1,r]查找
        else:
            l = mid + 1
    '''
    循环退出条件是l==r，此时mid==l，区间内只有一个数l(r)满足cnt>=k的最小值，
    假设l不在矩阵中，那么在矩阵中必然存在最大的y<l，且满足小于等于y的个数大于等于k，这就与l
    是最小值相矛盾！
    '''
    return l


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(kthSmallest(self, matrix, k))

from typing import List

from self import self


def partition(self, s: str) -> List[List[str]]:
    n = len(s)
    """
    注意python的这种初始化方式，不要写成dp=[[False]*n]*n，这样以来
    我们去给dp[i][j]赋值时，发现会对dp[j]整列赋值！
    dp=[[初始化值]*col for _ in range(cow)]
    """
    dp = [[False] * n for _ in range(n)]

    # i>=j时，dp[i][j]是True
    for i in range(0, n):
        for j in range(0, i + 1):
            dp[i][j] = True
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

    ans = []
    cur_list = []

    def dfs(i: int):
        if i == n:
            ans.append(cur_list[:])
            return
        for j in range(i, n):
            if dp[i][j]:
                cur_list.append(s[i:j + 1])
                dfs(j + 1)
                cur_list.pop()

    dfs(0)
    return ans


s = "cdd"
print(partition(self, s))

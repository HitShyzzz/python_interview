from typing import List

from self import self


def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    if k == 0:
        return [0] * n
    copy = code * 3
    ans = [0] * n
    if k < 0:
        for i in range(n - 1, n + k - 1, -1):
            ans[0] += copy[i]
        for i in range(1, n):
            ans[i] = ans[i - 1] - copy[i - 1 + n + k] + copy[i - 1 + n]
    else:
        for i in range(n, n + k):
            ans[n - 1] += copy[i]
        for i in range(n - 2, -1, -1):
            ans[i] = ans[i + 1] - copy[i + 1 + n + k] + copy[i + 1 + n]
    return ans


code = [5, 7, 1, 4]
k = 3
print(code * 3)
print(decrypt(self, code, k))

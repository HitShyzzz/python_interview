from typing import List

from self import self


# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    import functools
    """
    functools库中的lru_cache给当前函数加了装饰器，可以将当前函数计算的结果缓存起来，
    并在缓存满的情况下按照lru(最近最少使用)原则换出。
    适用于当前函数存在大规模重复计算场景
    不用lru_cache装饰器会超时！
    """
    @functools.lru_cache(None)
    def dfs(s: str) -> bool:
        if not s:
            return True
        ans = False
        for i in range(1, len(s) + 1):
            if s[0:i] in wordDict:
                ans = dfs(s[i:]) or ans
        return ans

    return dfs(s)


s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(self, s, wordDict))

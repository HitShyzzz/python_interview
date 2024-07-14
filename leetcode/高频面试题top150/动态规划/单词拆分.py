from typing import List

from self import self


# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(0, i):
            if s[j:i] in wordDict:
                dp[i] = dp[j]
                if dp[i]:
                    break
    return dp[n]


s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(self, s, wordDict))

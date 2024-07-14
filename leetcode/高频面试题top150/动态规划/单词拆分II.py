from typing import List
from self import self


# 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# 输出:["cats and dog","cat sand dog"]

def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    import functools
    @functools.lru_cache(None)
    def backtrack(index: int) -> List[List[str]]:
        if index == len(s):
            return [[]]
        ans = []
        for i in range(index + 1, len(s) + 1):
            word = s[index:i]
            if word in wordSet:
                next_list = backtrack(i)
                for next_word in next_list:
                    ans.append([word] + next_word)
        return ans

    wordSet = set(wordDict)
    ans_list = backtrack(0)
    return [" ".join(word) for word in ans_list]


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(self, s, wordDict))

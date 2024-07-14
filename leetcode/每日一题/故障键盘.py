from self import self


# 输入：s = "poiinter"
# 输出："ponter"
def finalString(self, s: str) -> str:
    ans = ""
    for i in range(0, len(s)):
        if s[i] == 'i':
            ans = ans[::-1]
        else:
            ans = ans + s[i]
    return str(ans)


s = "poiinter"
print(finalString(self, s))

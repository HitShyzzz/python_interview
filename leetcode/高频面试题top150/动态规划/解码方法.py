from self import self


def numDecodings(self, s: str) -> int:
    n = len(s)
    dp = [0] * n
    dp[0] = 1 if s[0] != '0' else 0
    for i in range(1, n):
        if s[i] != '0':
            dp[i] = dp[i - 1]
        if s[i - 1] != '0' and int(s[i - 1]) * 10 + int(s[i]) <= 26:
            dp[i] = dp[i] + (1 if i < 2 else dp[i - 2])
    return dp[n - 1]


print(numDecodings(self, "226"))

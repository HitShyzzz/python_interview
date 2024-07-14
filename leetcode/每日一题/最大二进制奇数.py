from self import self


# 1010010
# 100011-->110001
def maximumOddBinaryNumber(self, s: str) -> str:
    a = s.count('1')
    b = len(s) - a
    return '1' * (a - 1) + '0' * b + '1'


s = "1010010"
print(maximumOddBinaryNumber(self, s))

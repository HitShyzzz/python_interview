from typing import List

import self as self


def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
        return []

    total_gpt = []
    # 0对括号
    total_gpt.append([None])
    # 1对括号
    total_gpt.append(["()"])
    # f[n]="("+f[n-1-i]+")"+f[i],i=0,1,...n-1
    for i in range(2, n + 1):
        l = []
        for j in range(i):
            list1 = total_gpt[j]
            list2 = total_gpt[i - 1 - j]
            for k1 in list1:
                for k2 in list2:
                    if k1 == None:
                        k1 = ""
                    if k2 == None:
                        k2 = ""
                    dp_i = "(" + k1 + ")" + k2
                    l.append(dp_i)
        total_gpt.append(l)

    return total_gpt[n]


str = generateParenthesis(self, 3)
print(str)

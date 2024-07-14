from typing import List

from self import self


# 输入：title = "capiTalIze tHe titLe"
# 输出："Capitalize The Title"
def capitalizeTitle(self, title: str) -> str:
    res = []
    for word in title.split():
        if len(word) <= 2:
            res.append(word.lower())
        else:
            res.append(word[0].upper() + word[1:].lower())
    return " ".join(res)


title = "capiTalIze OF titLe"
ans = capitalizeTitle(self, title)
print(ans)

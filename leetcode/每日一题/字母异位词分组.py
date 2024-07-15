from typing import List

from self import self

'''
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = []
    # key是排序后的字符串，value是异位词list
    group_dict = {}
    for s in strs:
        key = "".join(sorted(s))
        group_list = group_dict.get(key, [])
        group_list.append(s)
        group_dict[key] = group_list
    for _, value in group_dict.items():
        ans.append(value)
    return ans


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(self, strs))
s = 'adc'
print("".join(sorted(s)))
print(s)

# class Solution:
#     def groupStrings(self, strings: List[str]) -> List[List[str]]:
#         ans = {}
#         for s in strings:
#             flag = True
#             for i in range(1, len(s)):
#                 if not (ord(s[i]) - ord(s[i-1]) == 1 or (s[i-1] == 'z' and s[i]=='a')):
#                     flag = False
#                     break
#             if flag:
#                 if len(s) in ans.keys():
#                     ans[len(s)].append(s)
#                 else:
#                     ans[len(s)] = [s]
#         res = []
#         ans = sorted(ans.items(), key=lambda x: x[0], reverse=True)
#         for x in ans:
#             res.append(x[1])
#         return res


def getKey(s) -> str:
    # a-> 0, b = 1, z-> 25
    # z - a = 25
    # ( a - b  + 26 ) % 26 = 25
    res = ''
    for i in range(1, len(s)):
        gap_str = str((ord(s[i]) - ord(s[i - 1]) + 26) % 26)
        res += gap_str.zfill(2)
    return res

print(getKey('acef'))
"""
leetcode 1249 移除无效的括号
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # left ( num >= right ) num
        left_num, right_num = 0, 0
        s = list(s)
        ans = []
        for i, x in enumerate(s):
            if x == '(':
                left_num += 1
                ans.append(x)
            elif x == ')':
                if right_num < left_num:
                    right_num += 1
                    ans.append(x)
            else:
                ans.append(x)
        index = len(ans) - 1
        while left_num > right_num:
            if ans[index] == '(':
                left_num -= 1
                ans = ans[:index] + ans[index+1:]
            index -= 1
        return ''.join(ans)
"""
leetcode 1249 移除无效的括号

给你一个由 '('、')' 和小写字母组成的字符串 s。
你需要从字符串中删除最少数目的 '(' 或者 ')'（可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

示例 1：
输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # left ( num >= right ) num
        left_num, right_num = 0, 0
        s = list(s)
        ans = []
        # 控制左括号数大于等于右括号数
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
        # 删除多余左括号
        index = len(ans) - 1
        while left_num > right_num:
            if ans[index] == '(':
                left_num -= 1
                ans = ans[:index] + ans[index+1:]
            index -= 1
        return ''.join(ans)
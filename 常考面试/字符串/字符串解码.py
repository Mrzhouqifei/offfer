"""
leetcode 394 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

输入：s = "3[a]2[bc]"
输出："aaabcbc"
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (str, int) 记录之前的字符串和括号外的上一个数字
        num = 0
        res = ""  # 实时记录当前可以提取出来的字符串
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0
            elif c == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += c
        return res


class Solution:
    def decodeString(self, s: str) -> str:
        pattern = re.compile(r'(\d+)\[(\w+)\]')
        m = pattern.findall(s)
        while m:
            for num, char in m:
                s = s.replace(f'{num}[{char}]', char * int(num))
            m = pattern.findall(s)
        return s


import re

pattern = re.compile('(\d+)\[(\w+)\]')
m = pattern.findall('3[a2[c]]')
print(m)

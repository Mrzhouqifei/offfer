"""
leetcode 5 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not n:
            return ""
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1

        max_len = 1
        res = s[0]

        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    f[i][j] = s[i] == s[j]
                else:
                    f[i][j] = f[i+1][j-1] & (s[i] == s[j])
                if f[i][j] and length > max_len:
                    max_len = length
                    res = s[i:j+1]
        return res

"""
leetcode 516最长回文子序列
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
输入:
"bbbab"
输出:
4
一个可能的最长回文子序列为 "bbbb"。
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 动态窗口
        if not s:
            return 0
        n = len(s)
        dp = [[1]*n for _ in range(n)]

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    if i + 1 <= j -1:
                        dp[i][j] = max(dp[i][j], dp[i+1][j-1]+2)
                    else:
                        dp[i][j] = 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]



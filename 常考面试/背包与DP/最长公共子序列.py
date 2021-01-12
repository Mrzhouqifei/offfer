"""
leetcode 1143 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

示例 1:
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        if len1 == 0 or len2 == 0:
            return 0
        f = [[0] * (len2+1) for _ in range(len1+1)]  # 包含0个数，1个数.....
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                f[i][j] = max(f[i-1][j-1] + (text1[i-1] == text2[j-1]), f[i-1][j], f[i][j-1])
        return f[len1][len2]
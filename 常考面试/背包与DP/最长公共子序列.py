"""
leetcode 1143
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
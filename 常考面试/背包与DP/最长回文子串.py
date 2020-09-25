class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not n:
            return ""
        f = [[0] * n for _ in range(n)]  # i ->子序列除了自身还有多长
        for i in range(n):
            f[0][i] = 1

        max_len = 1
        res = s[0]
        for i in range(1, n):
            for j in range(n-i):
                f[i][j] = ((i == 1) | f[i - 2][j + 1]) & (s[j] == s[j + i])
                # f[i][j] = ((i == 1) & (s[j] == s[j+1])) | ((i >= 2) & f[i-2][j+1] & (s[j] == s[j+i]))
                if f[i][j] and i + 1 > max_len:
                    max_len = i + 1
                    res = s[j:j+i+1]
        return res
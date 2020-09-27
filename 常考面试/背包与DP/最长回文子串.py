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
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1

        max_len = 0
        res = s[0]
        for i in range(1, n): # i除去自身的length
            for j in range(n - i):
                f[j][j+i] = (f[j+1][j+i-1] | (i == 1)) & (s[j] == s[j+i])

                if f[j][j+i] and i > max_len:
                    max_len = i
                    res = s[j:j+i+1]
        return res






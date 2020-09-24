class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        zeros = []
        ones = []

        for i in range(len(strs)):
            one, zero = 0, 0
            for x in strs[i]:
                if x == '0':
                    zero += 1
                else:
                    one += 1
            zeros.append(zero)
            ones.append(one)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for k in range(len(strs)):
            for i in range(m, zeros[k]-1, -1):
                for j in range(n, ones[k]-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros[k]][j - ones[k]] + 1)
        return dp[m][n]



s = Solution()
ans = s.findMaxForm(["10","0001","111001","1","0"], 5, 3)
print(ans)

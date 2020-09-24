class Solution:
    def findDerangement(self, n: int) -> int:
        mod = int(1e9) + 7
        dp = [0] * (n+1)
        dp[1] = 0
        if n > 1:
            dp[2] = 1
        for i in range(3, n+1):
            dp[i] = ((i-1) * (dp[i-1] + dp[i-2])) % (mod)
        return dp[n]

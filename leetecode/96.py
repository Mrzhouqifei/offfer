class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(0, n+1):
            if i ==0 or i==1:
                dp[i] = 1
                continue
            for j in range(1, i+1):
                dp[i] = dp[i] + dp[j-1] * dp[i-j]
        return dp[n]
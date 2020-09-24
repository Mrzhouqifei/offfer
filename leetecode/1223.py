class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        max_time = max(rollMax)
        dp = [[[0] * (max_time+1) for _ in range(7)] for __ in range(n+1)]
        mod = 10 ** 9 + 7
        """
        k=1: dp[i][j][1] = sum(dp[i-1][other][:])
        k>1: dp[i][j][k] = dp[i-1][j][k-1]
        i个数，j结尾，出现k次
        """
        for i in range(1, n+1):
            for j in range(1, 7):
                if i == 1:
                    dp[i][j][1] = 1
                    continue
                for k in range(1, rollMax[j-1]+1):
                    if k == 1:
                        dp[i][j][1] = 0
                        for jj in range(1, 7):
                            if jj != j:
                                for kk in range(1, rollMax[jj-1]+1):
                                    dp[i][j][1] += dp[i-1][jj][kk]
                                    dp[i][j][1] %= mod
                    else:
                        dp[i][j][k] = dp[i-1][j][k-1]
        res = 0
        for j in range(1, 7):
            for k in range(1, rollMax[j-1] + 1):
                res += dp[n][j][k]
                res %= mod
        return res
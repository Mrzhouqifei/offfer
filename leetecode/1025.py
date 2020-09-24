class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [0] * (N+1)
        if N <= 1:
            return False
        else:
            dp[2] = 1
            for i in range(3, N+1):
                for x in range(1, i // 2):
                    if dp[x] == 0 and i % x == 0:
                        dp[i] = 1
                        break
            if dp[N]:
                return True
            else:
                return False


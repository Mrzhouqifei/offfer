n, V = list(map(int, input().split()))
dp = [0] * (V+1)
for i in range(n):
    v, w = list(map(int, input().split()))
    for j in range(v, V+1):
        dp[j] = max(dp[j], dp[j-v]+w)
print(dp[-1])


"""
面试题 08.11. 硬币
"""

class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        dp = [1] + [0] * n
        for coin in coins:
            for j in range(coin, n+1):
                dp[j] = (dp[j] + dp[j - coin]) % 1000000007
        return dp[n]

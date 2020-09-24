class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [float('inf')] * (amount + 1)
        f[0] = 0
        n = len(coins)
        coins = sorted(coins, reverse=True)
        for i in range(n):
            for j in range(coins[i], amount+1):
                f[j] = min(f[j], f[j-coins[i]] + 1)
        if f[amount] > 9999999999:
            return -1
        else:
            return f[amount]
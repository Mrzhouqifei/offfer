class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        f = [0] * (amount + 1)
        f[0] = 1

        for i in range(n):
            for j in range(coins[i], amount + 1):
                f[j] += f[j - coins[i]]
        return f[amount]

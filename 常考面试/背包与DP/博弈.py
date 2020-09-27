"""
硬币游戏
nim游戏 292
预测赢家 leetcode 486
石子游戏 leetcode 877
"""

# 硬币游戏通用解法
# 对手状态全是必胜，那么我必败
# 对手一个一个必败状态，那么我必胜
class Solution:
    def canWinNim(self, n: int) -> bool:
        # f[0] = False
        # f[n] = not (f[n-s[0]] & f[n-s[1]] & f[n-s[2]])
        if n == 0:
            return False
        if n <= 3:
            return True
        f = [False] * (n + 1)

        s = [1, 2, 3]

        f[1] = f[2] = f[3] = True
        for i in range(4, n + 1):
            for x in s:
                f[i] |= not f[i - x]
        return f[n]


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [[0] * n for _ in range(n)]  # 记录当前玩家得分减去对方玩家得分的最大值
        for i in range(n): f[i][i] = nums[i]

        for len in range(2, n+1):
            for i in range(n - len + 1):
                j = i + len - 1
                f[i][j] = max(nums[i] - f[i+1][j], nums[j] - f[i][j-1])
        return f[0][n-1] >= 0


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        f = [[0] * n for _ in range(n)]

        for i in range(n): f[i][i] = piles[i]

        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                f[i][j] = max(piles[i] - f[i+1][j], piles[j] - f[i][j-1])
        return f[0][n-1] > 0
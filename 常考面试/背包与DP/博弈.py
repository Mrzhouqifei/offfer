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

        for i in range(1, n + 1):
            for x in s:
                if i - x >= 0:
                    f[i] |= not f[i - x]
        return f[n]


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

"""
486
给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。
每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [[0] * n for _ in range(n)]  # [起点, 终点]记录当前玩家得分减去对方玩家得分的最大值
        for i in range(n): f[i][i] = nums[i]

        for len in range(2, n+1):
            for i in range(n - len + 1):
                j = i + len - 1
                f[i][j] = max(nums[i] - f[i+1][j], nums[j] - f[i][j-1])
        return f[0][n-1] >= 0

"""
877
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        f = [[0] * n for _ in range(n)]

        for i in range(n): f[i][i] = piles[i]

        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                f[i][j] = max(piles[i] - f[i+1][j], piles[j] - f[i][j-1])
        return f[0][n-1] >= 0
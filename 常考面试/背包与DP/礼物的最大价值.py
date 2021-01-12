"""
剑指offer 47 礼物的最大价值
一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
输入:
[
[1,3,1],
[1,5,1],
[4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
"""

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # f[i][j] = max(f[i-1][j], f[i][j-1]) + grid[i][j]
        m, n = len(grid), len(grid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1]) + grid[i-1][j-1]    # 所以下标要从1开始
        return f[m][n]
    # 数组中的逆序对


"""
面试题 16.19. 水域大小
"""


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        def dfs(i, j):
            nonlocal num

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and land[x][y] == 0:
                    num += 1
                    land[x][y] = 1
                    dfs(x, y)

        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    num = 1
                    land[i][j] = 1
                    dfs(i, j)
                    res.append(num)

        return sorted(res)


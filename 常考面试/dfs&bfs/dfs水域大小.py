
"""
面试题 16.19. 水域大小
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。
由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，
返回值需要从小到大排序。

输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
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


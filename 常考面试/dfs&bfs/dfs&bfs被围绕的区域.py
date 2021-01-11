"""
130. 被围绕的区域

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = 'A'
                for dx, dy in dirs:
                    dfs(x + dx, y + dy)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'



"""
bfs
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = []

        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][n - 1] == 'O':
                q.append((i, n - 1))

        for i in range(n):
            if board[0][i] == "O":
                q.append((0, i))
            if board[m - 1][i] == 'O':
                q.append((m - 1, i))

        while q:
            i, j = q.pop(0)
            board[i][j] = 'A'
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    q.append((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"








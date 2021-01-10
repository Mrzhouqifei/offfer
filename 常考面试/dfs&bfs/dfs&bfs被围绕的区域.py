"""
130. 被围绕的区域
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = 'A'
                dfs(x + 1, y)
                dfs(x, y + 1)
                dfs(x - 1, y)
                dfs(x, y - 1)

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
            print(i, j)
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








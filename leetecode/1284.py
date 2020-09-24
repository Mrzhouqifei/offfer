# class Solution:
    # def minFlips(self, mat: List[List[int]]) -> int:
import copy



def minFlips(mat):
    from queue import Queue
    # n row, m column
    def encoder(mat, n, m):
        x = 0
        for i in range(n):
            for j in range(m):
                x = (x << 1) + mat[i][j]
        return x

    def decoder(x, n, m):
        mat = [[0] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mat[i][j] = x & 1
                x = x >> 1
        return mat

    def convert(status, n, m, i, j):
        for d in [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]:
            xi, yj = i + d[0], j + d[1]
            if 0 <= xi < n and 0 <= yj < m:
                status[xi][yj] = status[xi][yj] ^ 1

    step = 0
    n, m = len(mat), len(mat[0])
    visited = set()
    q = Queue()
    status = encoder(mat, n, m)
    if status == 0:
        return step
    q.put_nowait(status)
    visited.add(status)

    while not q.empty():
        step += 1
        size = q.qsize()
        for _ in range(size):
            status = decoder(q.get_nowait(), n, m)

            for i in range(n):
                for j in range(m):
                    convert(status, n, m, i, j)
                    x = encoder(status, n, m)
                    if x == 0:
                        return step
                    if x not in visited:
                        visited.add(x)
                        q.put_nowait(x)
                    convert(status, n, m, i, j)

    return -1

print(minFlips([[0,0],[0,1]]))
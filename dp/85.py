class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        psum = [[0] * (n+1) for _ in range(m)]

        for i in range(m+1):
            for j in range(n+1):
                psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + matrix[i-1][j-1]




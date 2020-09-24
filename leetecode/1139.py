class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_len = min(n, m)
        while max_len:
            for i in range(n-max_len+1):
                for j in range(m-max_len+1):
                    flag = True
                    for l in range(max_len):
                        if grid[i+l][j] == 0 or grid[i+l][j+max_len-1] == 0 or grid[i][j+l] == 0 or grid[i+max_len-1][j+l] == 0:
                            flag = False
                            break
                    if flag:
                        return max_len ** 2
            max_len -= 1
        return max_len ** 2
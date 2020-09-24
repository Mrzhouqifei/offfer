class Solution:
    def numSquares(self, n: int) -> int:
        square_set = set()
        for i in range(1, n+1):
            tmp = i*i
            if tmp > n:
                break
            else:
                square_set.add(tmp)
        square_list = list(square_set)
        square_list.sort()
        dp = [9999999] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            if i in square_set:
                dp[i] = 1
            else:
                for square in square_list:
                    if square > i:
                        break
                    j = i - square
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]
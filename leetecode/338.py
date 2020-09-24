class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        if num >= 1:
            dp[1] = 1
        b = 2
        while b <= num:
            dp[b] = 1
            for x in range(1, b):
                if x + b > num:
                    break
                dp[x+b] = dp[x] + 1
            b <<= 1
        return dp
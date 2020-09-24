class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        elif n <= 10:
            dp = [10]
            for i in range(2, n+1):
                tmp = 9
                for j in range(9, 10-i, -1):
                    tmp *= j
                dp.append(dp[-1] + tmp)
            return dp[-1]
        else:
            dp = [10]
            n = 10
            for i in range(2, n + 1):
                tmp = 9
                for j in range(9, 10 - i, -1):
                    tmp *= j
                dp.append(dp[-1] + tmp)
            return dp[-1]

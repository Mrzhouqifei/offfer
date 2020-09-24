class Solution:
    def cuttingRope(self, n: int) -> int:
        ans = 1
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        else:
            while n > 4:
                ans = ans * 3
                n -= 3
            ans = ans * n
            return ans
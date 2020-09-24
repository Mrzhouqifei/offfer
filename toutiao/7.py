class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 10:
            return x
        y = 0
        sgn = 1 if x > 0 else -1
        while abs(x) >= 1:
            y = y * 10 + (abs(x) % 10)
            x = x // 10
        return sgn * y
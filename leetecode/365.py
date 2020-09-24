import math
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        elif x == 0:
            return y == z
        elif y == 0:
            return x == z
        else:
            return z % math.gcd(x, y) == 0

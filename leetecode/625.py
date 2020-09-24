class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a <= 0:
            return 0
        if a<=9:
            return a


        res = []
        while a!=1:
            for i in range(9, 0, -1):
                if a % i == 0:
                    res.append(i)
                    a = a/i
                    break
            if i == 1:
                return 0
        r = 0
        res.reverse()
        for x in res:
            r = r*10+x
            if r > 999999999:
                return 0
        return r


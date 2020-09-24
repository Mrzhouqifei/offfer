class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        low_n, high_n = 0, 0
        for i in range(1, 11):
            if low / pow(10,i) < 1 and not low_n:
                low_n = i
            if high / pow(10,i) < 1 and not high_n:
                high_n = i
        res = set()
        def dfs(num, length):
            if len(num) == length:
                res.add(num)
                return
            else:
                last = int(num[-1])
                if last > 0:
                    dfs(num + str(last - 1), length)
                if last < 9:
                    dfs(num + str(last + 1), length)

        for length in range(low_n, high_n+1):
            for i in range(1, 10):
                dfs(str(i), length)

        if low_n == 1:
            res.add(0)
        final = []
        for x in res:
            x = int(x)
            if x>=low and x<=high:
                final.append(x)
        final.sort()
        return final


class Solution:
    def lexicalOrder(self, n: int):
        res = []
        def dfs(now, n):
            for i in range(10):
                tmp = now*10+i
                if tmp > n:
                    return
                res.append(tmp)
                dfs(tmp, n)

        for i in range(1, 10):
            res.append(i)
            dfs(i, n)
        return res
        # print(res)

solution = Solution()
solution.lexicalOrder(100)
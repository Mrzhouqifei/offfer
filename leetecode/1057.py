class Solution:
    def assignBikes(self, workers, bikes):
        def cal_dis(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        n_workers = len(workers)
        n_bikes = len(bikes)
        res = [-1] * n_workers
        q = list(range(n_bikes))
        dp = [[0]*n_bikes for _ in range(n_workers)]
        for i in range(n_workers):
            for j in range(n_bikes):
                dp[i][j] = cal_dis(workers[i], bikes[j])
        while len(q) > 0:
            bike = q.pop()
            tmpi = -1
            min_dis = 9999999
            for i in range(n_workers):
                if dp[i][bike] < min_dis:
                    if res[i]==-1:
                        if tmpi != -1:
                            res[tmpi] = -1
                        min_dis = dp[i][bike]
                        res[i] = bike
                        tmpi = i
                    elif dp[i][bike] < dp[i][res[i]] or (dp[i][bike] == dp[i][res[i]] and bike < res[i]):
                        if tmpi != -1:
                            res[tmpi] = -1
                        q.append(res[i])
                        min_dis = dp[i][bike]
                        res[i] = bike
                        tmpi = i
        return res


solution = Solution()
solution.assignBikes([[0,0],[2,1]], [[1,2],[3,3]])
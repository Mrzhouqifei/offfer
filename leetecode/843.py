class Solution:
    def findSecretWord(self, wordlist, master):
        def cal_dis(x, y):
            same = 0
            for i in range(6):
                if x[i] == y[i]:
                    same += 1
            return same
        n = len(wordlist)
        visited = [0]*n
        for _ in range(10):
            min_remain = 999999
            tmp = 0
            for i in range(n):
                if visited[i] == 0:
                    dp = [0] * 7
                    for j in range(n):
                        if visited[j] == 0 and i!=j:
                            dp[cal_dis(wordlist[i], wordlist[j])] += 1
                    max_ = max(dp)
                    if max_ < min_remain:
                        min_remain = max_
                        tmp = i
            res = master.guess(wordlist[tmp])
            visited[tmp] = 1
            for j in range(n):
                if visited[j] == 0 and cal_dis(wordlist[tmp], wordlist[j]) != res:
                    visited[j] = 1
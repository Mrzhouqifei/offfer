class Solution:
    def findContestMatch(self, n: int):
        s = dict()
        for i in range(1, n // 2 + 1):
            s[i] = "("+str(i)+","+str(n+1-i)+")"
        sorted(s)
        while len(s) > 1:
            tmp = s
            tmp_n = len(tmp)
            s = dict()
            tmp_len = len(tmp)
            for i in range(1, tmp_len // 2 + 1):
                s[i] = "(" + tmp[i] + "," + tmp[tmp_n + 1 - i] + ")"
            sorted(s)
        print(s)

s = Solution()
s.findContestMatch(10)




class GoUpstairs:
    def countWays(self, n):
        # write code here
        pre, now = 1, 2
        if n == 1:
            return pre
        elif n == 2:
            return now
        else:
            for i in range(3, n+1):
                tmp = (pre + now) % 1000000007
                pre = now
                now = tmp
            return now

a = GoUpstairs()
print(a.countWays(3))
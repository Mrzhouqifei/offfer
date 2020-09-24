from queue import PriorityQueue
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = PriorityQueue()
        q.put_nowait(1)
        ugly = set([1])
        while len(ugly) < n*2:
            tmp = q.get_nowait()
            t1, t2, t3 = tmp*2, tmp*3, tmp*5
            if t1 not in ugly:
                q.put_nowait(t1)
            if t2 not in ugly:
                q.put_nowait(t2)
            if t3 not in ugly:
                q.put_nowait(t3)
            ugly.add(t1)
            ugly.add(t2)
            ugly.add(t3)
        ugly = list(ugly)
        ugly.sort()
        return ugly[n-1]
class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        n = len(bulbs)
        t_bulb = [0] * n
        for i in range(n):
            t_bulb[bulbs[i]-1] = i + 1

        flag = False
        res = 9999
        i = 0
        while i < len(t_bulb)-K-1:
            j = i + K + 1
            t = True
            for p in range(i+1, j):
                if t_bulb[p] < t_bulb[j] or t_bulb[p] < t_bulb[i]:
                    t = False
                    i = p
                    break
            if t:
                bila_max = max(t_bulb[i], t_bulb[j])
                res = min(res, bila_max)
                i = j
                flag = True
        if flag:
            return res
        return -1

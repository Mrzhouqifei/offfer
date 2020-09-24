class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        aSet = set(A)
        aAppear = set()
        repeat = []
        for x in A:
            if x not in aAppear:
                aAppear.add(x)
            else:
                repeat.append(x)
        if len(repeat) == 0:
            return 0
        repeat = sorted(repeat)
        minA = min(A)
        j, nj, res = 0, len(repeat), 0
        for i in range(minA+1, 90000):
            if j == nj:
                break
            if i not in aSet and i > repeat[j]:
                res += (i - repeat[j])
                j += 1
        return res







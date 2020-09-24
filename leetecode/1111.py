class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        n = len(seq)
        d = 0
        for i in range(n):
            if seq[i] == '(':
                d += 1
                ans.append(d % 2)
            else:
                ans.append(d % 2)
                d -= 1
        return ans
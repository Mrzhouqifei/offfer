class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def get_count(prefix, n):
            count = 0
            next = prefix + 1
            cur = prefix
            while cur <= n:
                count += min(n+1, next) - cur
                cur *= 10
                next *= 10
            return count

        p, prefix = 1, 1
        while(p<k):
            count = get_count(prefix, n)
            if p+count > k:
                prefix *= 10
                p += 1
            elif p+count <= k:
                prefix += 1
                p+=count
        return prefix
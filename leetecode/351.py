class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        from collections import deque
        import copy
        q = deque()
        for i in range(3):
            for j in range(3):
                q.append([i*3+j])
        step, count = 1, 0
        if m == 1:
            count = 9
        if n == 1:
            return count
        all = set(range(9))

        def isValid(tmp_c, x, i, j):
            ni, nj = x//3, x%3
            sub1, sub2 = abs(ni-i), abs(nj-j)
            if (sub1==2 and sub2==2) or (sub1==2 and sub2==0) or (sub1==0 and sub2==2):
                if ((ni + i) / 2 * 3 + (nj + j) / 2) not in tmp_c:
                    return False
            return True

        while len(q) > 0:
            step += 1
            size = len(q)
            for _ in range(size):
                tmp = q.popleft()
                i = tmp[-1]//3
                j = tmp[-1]%3
                for x in list(all.difference(set(tmp))):
                    tmp_c = copy.deepcopy(tmp)
                    if isValid(tmp_c, x, i, j):
                        tmp_c.append(x)
                        q.append(tmp_c)
                        if step >= m:
                            count+=1

            if step >= n:
                break
        return count

# solution =Solution()
# print(solution.numberOfPatterns(1,2))
from queue import Queue
import copy
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1)]
        q = Queue()
        q.put_nowait([(0, 0)])
        n, m = len(grid), len(grid[0])
        res = []
        def cal_dis(tmp_list):
            r = 0
            for t in tmp_list:
                r += grid[t[0]][t[1]]
            return r
        while not q.empty():
            tmp_list = q.get_nowait()
            if len(tmp_list) == n + m -1:
                res.append(cal_dis(tmp_list))
            else:
                tmp = tmp_list[-1]
                for dir in dirs:
                    t0 = tmp[0] + dir[0]
                    t1 = tmp[1] + dir[1]
                    if t0 < n and t1 < m:
                        tmp_c = copy.deepcopy(tmp_list)
                        tmp_c.append((t0, t1))
                        q.put_nowait(tmp_c)
        return min(res)


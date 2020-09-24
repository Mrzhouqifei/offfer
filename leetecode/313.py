from queue import PriorityQueue

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = PriorityQueue()
        q.put_nowait(1)
        visited = set([1])
        for i in range(n):
            tmp = q.get_nowait()
            for x in primes:
                t = tmp * x
                if t not in visited:
                    q.put_nowait(t)
                    visited.add(t)
        return q.get_nowait()


# names = list(map(str, input().split(',')))
# if len(names) == 0:
#     print('error.0001')
# else:
#     dicts = dict()
#     flag = True
#     for name in names:
#         for c in name:
#             if c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
#                 flag=False
#                 print('error.0001')
#                 break
#         if name in dicts.keys():
#             dicts[name] += 1
#         else:
#             dicts[name] = 1
#     if flag:
#         sort_keys = sorted(dicts, key=dicts.__getitem__,reverse=True)
#         max_num = dicts[sort_keys[0]]
#         res = []
#         for x in sort_keys:
#             if dicts[x] == max_num:
#                 res.append(x)
#             else:
#                 break
#         res.sort()
#         print(res[0])

# Tom,Lily,Tom,Lucy,Lucy,Jack
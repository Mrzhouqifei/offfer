from queue import Queue
import copy
nums = list(map(int, input().split()))
cost = dict()
next = dict()
na = False
start = []
for _ in range(nums[0]):
    tmp = list(map(int, input().split()))
    if len(tmp) > 1:
        if len(cost) == 0:
            start.append([tmp[0]])
            start.append(tmp[1])
        cost[tmp[0]] = tmp[1]
        next[tmp[0]] = tmp[2:]
    else:
        na = True
        print('NA')
        break
if not na:
    max_res = -9999
    q = Queue()
    q.put_nowait([start[0], start[1]])
    digui = False
    while (not q.empty()) and (not digui):
        t = q.get_nowait() # t[0] list, t[1] cost
        if len(next[t[0][-1]]) == 0:
            max_res = max(max_res, t[1])
        else:
            for ne in next[t[0][-1]]:
                if ne in t[0]:
                    digui = True
                    print('R')
                    break
                tmp = copy.deepcopy(t[0])
                tmp.append(ne)
                tmp1 = t[1] + cost[ne]
                q.put_nowait([tmp, tmp1])
    if not digui:
        print(max_res)

'''
5 2 3 1 0 0
1 20 2 3
2 30 3 4 5
3 50 4
4 60
5 80
'''


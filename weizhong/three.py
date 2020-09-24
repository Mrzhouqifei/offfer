n = int(input())
if n == 0:
    print(0)
else:
    lists = []
    money = 0
    can = 1
    for i in range(n):
        tmp = list(map(int, input().split()))
        if tmp[1] > 0:
            money += tmp[0]
            can -= 1
            can += tmp[1]
        else:
            lists.append(tmp[0])
    lists.sort()
    while len(lists)>0 and can > 0:
        can -= 1
        money += lists.pop()
    print(money)




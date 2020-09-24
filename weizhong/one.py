n, m, a, b = list(map(int, input().split()))
if m % n == 0:
    print(0)
else:
    num = n - m % n
    liwu = num * b
    hongbao = []
    hongbao.append(liwu)
    leave = 0
    while True:
        leave += 1
        hongbao_monney = leave * a
        remain = n - leave
        if m % remain != 0:
            num = remain - m % remain
            if remain > 1:
                hongbao_monney += num * b
            hongbao.append(hongbao_monney)
        else:
            hongbao.append(hongbao_monney)
            break
    # print(hongbao)
    min_m = min(hongbao)
    print(min_m)


'''
n, m, a, b = list(map(int, input().split()))
if m % n == 0:
    print(0)
else:
    num = n - m % n
    liwu = num * b
    hongbao = []
    hongbao.append(liwu)
    leave = 0
    while m % (n-leave) !=0:
        leave += 1
        hongbao_monney = leave * a
        remain = n - leave
        # print(remain)
        if remain > 1:
            hongbao_monney += (remain - m % remain) * b
        hongbao.append(hongbao_monney)
    # print(hongbao)
    min_m = min(hongbao)
    print(min_m)

'''
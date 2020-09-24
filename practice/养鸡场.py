'''
1.有n个养鸡场，每个养鸡场初始的鸡数目是a[i]。每天早上都向各个养鸡场新增k只鸡；每天结束的时候，从鸡数目最多的养鸡场中卖掉一半的鸡。
问：m天后，n个养鸡场中鸡的总数是多少？
例如，养鸡场数目n=3，各个鸡场初始的鸡数目分别是{100,200,400}，k=100，则m=3天后，还剩下的鸡的数目是925。

2.给出一个包含n个整数的序列，从中任意选出一个子序列，求子序列最大值的期望？例如，从{1,2,3}中任意选出一个子序列，
以3作为最大值的子序列有3个，以2作为最大值的子序列有2个，以1作为最大值的子序列有1个，故最大值的期望为 3*3/6 + 2*2/6 + 1*1/6 = 2.333333
'''

n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort(reverse=True)

for day in range(m):
    for i in range(n):
        a[i] = a[i] + k
    v = a.pop(0) // 2
    flag = True
    for j, x in enumerate(a):
        if v > x:
            flag = False
            a.insert(j, v)
            break
    if flag:
        a.append(v)
    # a.append(v)
    # a.sort(reverse=True)
print(sum(a))

'''

有位老铁设计了一个跳格子游戏，游戏有N个格子顺序排成一行，编号从1到N，每个格子有点数Qi，有标记Li（标记的范围是1-M），
每次跳格子，要选择一个格子a，以任意正偶数距离x跳到格子b，如果格子b在游戏区域内，且La=Lb，则称为一次合法跳跃，
获得的分数是(a + b) * (Qa + Qb)。

在继续设计游戏玩法时，这位老铁纠结了很久，于是他决定放弃……但是他想知道所有合法跳跃总共能获得多少分。

输入描述:
第一行N，M，表示格子数和标记种类数，

第二行N个数，表示格子的点数

第三行N个数，表示每个格子的标记

输出描述:
一个整数P，表示总共能获得的分数，由于分数可能很大，这里只需要输出分数除以10007的余数

输入例子1:
5 2
1 2 3 4 5
1 2 1 2 1
'''

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
N, M = line1[0], line1[1]
Q = line2
L = line3
res = 0
for i in range(len(L)-1):
    for j in range(i+2, len(L), 2):
        if L[i] == L[j]:
            res += (i+1+j+1) * (Q[i]+Q[j])
            res = res % 10007

print(res)
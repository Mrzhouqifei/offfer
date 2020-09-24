"""
有n 个老铁（编号为 1 到n）正在玩丢手绢。在游戏里每人会把当前手里的手绢丢给一个固定的人，编号为Ti。 游戏开始时，
每人手里有自己的手绢。之后每一轮中，所有人会同时将自己当前手里的手绢全部丢给接收的对象。当有人重新拿到自己的手绢时，游戏结束。
那么游戏几轮会结束呢？

输入描述:
输入共 2 行。
第1 行包含 1 个正整数 n ，表示 n 个人。（n<=200000）
第2 行包含n 个用空格隔开的正整数T1,T2,… ,Tn，其中第Ti个整数表示编号为i 的同学会将手绢丢给编号为 Ti 的同学，Ti ≤n 且Ti ≠i。
保证游戏一定会结束。

输出描述:
输出共 1 行，包含 1 个整数，表示游戏可以进行多少轮。

输入例子1:
5
2 4 2 3 1


输出例子1:
3
"""

n = int(input())
T = list(map(int, input().split()))
dicts = dict()
dicts_new = dict()
for i in range(n):
    dicts[i] = list([i])
    dicts_new = []

for key in dicts.keys():
    v = dicts[key].pop()
    dicts_new[T[key]].append(v)
for key



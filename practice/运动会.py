"""
输入包括1+N行 第一行输入一个整数N, 1 <= N <= 10，表示今天要参加多少个讨论会 后续N行，
每行输入开始和结束时间，均为整数，用空格分隔，0 <= startTime < endTime <= 24
3
3 10
1 5
4 6
"""

# n = int(input())
# time = dict()
# for i in range(n):
#     l = list(map(int, input().split()))
#     time[l[0]] = l[1]
# order = list(sorted(time.keys()))
# end = 0
# flag = False
# for x in order:
#     if x < end:
#         print(-1)
#         flag = True
#         break
#     time_len = time[x] - x
#     end = time_len // 2 + 1 + x
# if not flag:
#     print(1)

n = int(input())
time = dict()
for i in range(n):
    l = list(map(int, input().split()))
    time[l[0]] = l[1]
order = list(sorted(time.keys()))
end = 0
flag = False
for x in order:
    if x < end:
        print(-1)
        flag = True
        break
    time_len = time[x] - x
    end = time_len // 2 + 1 + x
if not flag:
    print(1)

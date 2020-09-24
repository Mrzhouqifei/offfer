n = int(input())
arr = list(map(int, input().split()))
num = [1 for i in range(n)]

for i in range(n):
    # left
    for j in range(i-1, -1, -1):
        if arr[j] <= arr[i]:
            num[i] = num[i] + 1
        else:
            break
    # right
    for j in range(i+1, n):
        if arr[j] <= arr[i]:
            num[i] = num[i] + 1
        else:
            break

res = []
for i in range(n):
    res.append(arr[i]*num[i])
print(round(1.0 * sum(res) / sum(num), 6))
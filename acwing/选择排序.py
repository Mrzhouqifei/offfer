n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if nums[j] < nums[i]:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
for x in nums:
    print(x, end=' ')

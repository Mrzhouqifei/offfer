# 冒泡
n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    for j in range(n-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
for x in nums:
    print(x, end=' ')


# 选择（时间复杂度优于冒泡）

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


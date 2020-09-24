"""
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
"""


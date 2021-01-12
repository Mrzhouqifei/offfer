n = int(input())
nums = list(map(int, input().split()))


def quickSort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left, mid, right = [], [], []
    for x in nums:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            mid.append(x)
        else:
            right.append(x)
    return quickSort(left) + mid + quickSort(right)


nums = quickSort(nums)

for x in nums:
    print(x, end=' ')

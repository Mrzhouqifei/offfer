# # 归并排序是典型的二分分治排序
#
n = int(input())
nums = list(map(int, input().split()))


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    L = mergeSort(nums[:mid])
    R = mergeSort(nums[mid:])

    i, j, k = 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1
    return nums


nums = mergeSort(nums)
for x in nums:
    print(x, end=' ')

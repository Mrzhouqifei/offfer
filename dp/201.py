class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        if n == 0:
            return [-1, -1]
        first, last = n - 1, 0
        min_value, max_value = 999999, -999999
        for i in range(n-1, -1, -1):
            if array[i] > min_value:
                first = i
            else:
                min_value = array[i]
        for i in range(n):
            if array[i] < max_value:
                last = i
            else:
                max_value = array[i]

        if first > last:
            return [-1, -1]
        else:
            return [first, last]
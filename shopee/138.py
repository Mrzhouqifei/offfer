class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = list(str(n))
        length = len(stack)
        if length < 2:
            return -1
        for i in range(length-1, 0, -1):
            if stack[i-1] < stack[i]:
                min_index = i
                for j in range(i+1, length):
                    if stack[j] > stack[i-1]:
                        min_index = j
                tmp = stack[i-1]
                stack[i-1] = stack[min_index]
                stack[min_index] = tmp
                stack[i:] = stack[i:][::-1]
                stack = ''.join(stack)
                res = int(stack)
                if -2**31 < res < 2**31-1:
                    return res
                else:
                    return -1
        return -1
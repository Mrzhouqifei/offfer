class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        for i in range(n):
            max_num = max(num[i:])
            if num[i] == max_num:
                continue
            else:
                index = i
                for j in range(i+1, n):
                    if num[j] == max_num:
                        index = j
                tmp = num[i]
                num[i] = num[index]
                num[index] = tmp
                break
        return int(''.join(num))





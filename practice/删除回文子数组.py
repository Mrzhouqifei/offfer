class Solution:
    def minimumMoves(self, arr: List[int]) -> int:

        def remove(darr):
            res = 0
            length = len(darr)
            fix_flag = [True for i in range(length)]
            for i in range(length):
                gap = 1
                flag = fix_flag.copy()
                flag[i] = False
                while i - gap >= 0 and i + gap < length and darr[i - gap] == darr[i + gap]:
                    flag[i - gap] = False
                    flag[i + gap] = False
                new_arr = []
                for i in range(length):
                    if flag[i]:
                        new_arr.append(darr[i])
                res = max(res, 1 + remove(new_arr))
            return res

        return remove(arr)


class Solution:
    def myAtoi(self, str: str) -> int:
        '''
        + - 0-9 ' '
        '''
        max_int, min_int = 2**31 - 1, -2 ** 31
        res = ''
        flag = False
        sgn = 0
        intres = 0
        for c in str:
            if c == ' ' and not flag:
                continue
            elif(c >= '0' and c <= '9') and not flag:
                flag = True
                res += c
            elif c == '+' and not flag:
                flag = True
                sgn = 1
                res += c
            elif c == '-' and not flag:
                flag = True
                sgn = -1
                res += c
            elif (c >= '0' and c <= '9') and flag:
                res += c
            else:
                break
            if len(res) > 0:
                if sgn != 0:
                    intres = sgn * int(res[1:])
                else:
                    intres = int(res)
                if intres > max_int:
                    return max_int
                elif intres < min_int:
                    return min_int
        return intres

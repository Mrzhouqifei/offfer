class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = 1
        flag = False
        while not flag and length <= len(s) / 2:
            while len(s) % length != 0 and length <= len(s) / 2:
                length += 1
            if len(s) % length != 0:
                break

            pat = s[:length]

            flag = True
            start = length
            end = start + length  # 不包括
            while end <= len(s):
                if s[start:end] != pat:
                    flag = False
                    break
                start = end
                end = start + length
            length += 1
        if flag:
            return True
        else:
            return False



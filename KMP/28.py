class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            for i in range(len(haystack) - len(needle)):
                if haystack[i:len(needle)+i] == needle:
                    return i
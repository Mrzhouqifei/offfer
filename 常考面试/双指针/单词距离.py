"""
面试题 17.11. 单词距离
"""

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = float('inf'), float('-inf')
        res = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            elif words[i] == word2:
                p2 = i
            res = min(abs(p1 - p2), res)
        return res

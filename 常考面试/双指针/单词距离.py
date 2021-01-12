"""
面试题 17.11. 单词距离

有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。
示例：

输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1
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

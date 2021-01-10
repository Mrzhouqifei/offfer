"""
面试题 17.22. 单词转换
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:

        def transfer(a, b):
            num = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    num += 1
            if num == 1:
                return True
            else:
                return False

        def dfs(words, target):
            nonlocal wordList
            if words[-1] == target:
                return words

            for x in wordList:
                if x not in words and transfer(x, words[-1]):
                    words.append(x)
                    if len(dfs(words, target)) > 0:
                        return words
                    words.pop()
            wordList = [x for x in wordList if x not in words]   # 剪枝
            return []

        words = dfs([beginWord], endWord)
        return words


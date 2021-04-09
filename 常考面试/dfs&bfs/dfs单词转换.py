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
            return []

        words = dfs([beginWord], endWord)
        return words


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        length = len(beginWord)

        def transfer(a, b):
            num = 0
            for i in range(length):
                if a[i] != b[i]:
                    num += 1
                    if num > 1:
                        return False
            return True

        def dfs(words):
            nonlocal endWord, wordList

            if words[-1] == endWord:
                return words

            for x in wordList.copy():
                if x not in words and transfer(words[-1], x):
                    words.append(x)
                    if x in wordList:
                        wordList.remove(x)  # 剪枝

                    if len(dfs(words)) > 0:
                        return words
                    words.pop()

            return []

        if beginWord in wordList:
            wordList.remove(beginWord)
        words = dfs([beginWord])
        return words

"""
面试题 17.15. 最长单词

给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，
返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。

示例：

输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
输出： "dogwalker"
解释： "dogwalker"可由"dog"和"walker"组成。

"""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda x: (-len(x), x))

        def dfs(word, k):   # k代表从第k个单词往后
            if word == '':
                return True

            for j in range(k + 1, len(words)):
                if word[:len(words[j])] == words[j]:
                    if dfs(word[len(words[j]):], k):
                        return True
            return False

        for i in range(len(words) - 1):
            if dfs(words[i], i):
                return words[i]
        return ''
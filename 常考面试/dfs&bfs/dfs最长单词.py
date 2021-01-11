
"""
面试题 17.15. 最长单词
"""



# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         words = sorted(words, key=lambda x: (-len(x), x))
#
#         def dfs(word, k):
#             if word == '':
#                 return True
#
#             for j in range(k + 1, len(words)):
#                 if word[:len(words[j])] == words[j]:
#                     if dfs(word[len(words[j]):], k):
#                         return True
#             return False
#
#         for i in range(len(words) - 1):
#             if dfs(words[i], i):
#                 return words[i]
#         return ''

a, b = 1, 2
a, b = b, a
print(a, b)
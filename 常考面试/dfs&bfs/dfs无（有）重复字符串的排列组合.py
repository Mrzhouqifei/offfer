"""
面试题 08.07. 无重复字符串的排列组合
"""

class Solution:
    def permutation(self, S: str) -> List[str]:
        s = list(S)
        n = len(s)
        res = []
        def dfs(word, i):
            if i == n - 1:
                res.append(''.join(word))
                return

            for j in range(n):
                if s[j] not in word:
                    word.append(s[j])
                    dfs(word, i + 1)
                    word.pop()

        for j in range(n):
            dfs([s[j]], 0)
        return res

"""
面试题 08.08. 有重复字符串的排列组合
"""

class Solution:
    def permutation(self, S: str) -> List[str]:
        s = list(S)
        n = len(s)
        res = set()

        def dfs(word, i):
            if i == n - 1:
                words = [s[j] for j in word]    # words存的下标
                res.add(''.join(words))
                return

            for j in range(n):
                if j not in word:
                    word.append(j)
                    dfs(word, i + 1)
                    word.pop()

        for j in range(n):
            dfs([j], 0)
        return list(res)



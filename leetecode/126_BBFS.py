from collections import deque
import copy
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        return_res = []
        q = deque()
        q.append([beginWord])
        wordList = set(wordList)
        visited = set()
        flag = True
        numbers = 'abcdefghijklmnopqrstuvwxyz'
        word_length = len(endWord)
        while len(q) > 0 and flag:
            size = len(q)
            holds = wordList.difference(visited)
            for _ in range(size):
                tmp_res = q.popleft()
                tmp = tmp_res[-1]

                for j in range(word_length):
                    for x in numbers:
                        if x != tmp[j]:
                            new = tmp[:j] + x + tmp[j + 1:]
                            if new in holds:
                                tmp_res_c = copy.deepcopy(tmp_res)
                                if new == endWord:
                                    tmp_res_c.append(new)
                                    return_res.append(tmp_res_c)
                                    flag = False
                                else:
                                    tmp_res_c.append(new)
                                    q.append(tmp_res_c)
                                    visited.add(new)
        return return_res

# solution = Solution()
# a=solution.findLadders(
# "red",
# "tax",
# ["ted","tex","red","tax","tad","den","rex","pee"])
# print(a)

a = set()
b= set()
a.



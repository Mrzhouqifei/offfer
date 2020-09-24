class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        num = 0
        words = list(set(words))
        for word in words:
            flag = True
            word_len = len(word)
            for tmp in words:
                if len(tmp) > word_len and word == tmp[-word_len:]:
                    flag = False
                    break
            if flag:
                num += (word_len+1)
        return num
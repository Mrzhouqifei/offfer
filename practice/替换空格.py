# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = s.split(' ')
        ss = '%20'.join(res)
        return ss

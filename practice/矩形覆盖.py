# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        temp = 0
        last2 = 1
        last1 = 2
        for i in range(3,number+1):
            temp = last2 + last1
            last2 = last1
            last1 = temp
        return temp

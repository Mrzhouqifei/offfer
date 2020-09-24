"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            last2 = 0
            last1 = 1
            temp = 0
            for i in range(2, n+1):
                temp = last1 + last2
                last2 = last1
                last1 = temp
            return temp
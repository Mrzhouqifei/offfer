"""
面试题 17.09. 第 k 个数
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。
例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
示例 1:
输入: k = 5
输出: 9

由题设可知，起始的几个素数是1、3、5、7，其中基础因子是3、5、7;
后续的素数由3、5、7这三个数互相乘法结合(也就是因式分解后只有3、5、7这3个因子);
"""

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        num1, num2, num3 = 0, 0, 0
        q = [1]
        for i in range(1, k):
            next_num = min(q[num1] * 3, q[num2] * 5, q[num3] * 7)
            q.append(next_num)
            if next_num == q[num1] * 3:
                num1 += 1
            if next_num == q[num2] * 5:
                num2 += 1
            if next_num == q[num3] * 7:
                num3 += 1
        return q[-1]





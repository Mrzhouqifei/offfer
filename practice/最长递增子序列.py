"""
输出两行，第一行包括一个正整数n（n<=100000），代表数组长度。第二行包括n个整数，代表数组arr \left(1 \leq arr_i \leq 1e9 \right)(1≤arr
i ≤1e9)。

输出描述:
输出一行。代表你求出的最长的递增子序列。
示例1
输入
9
2 1 5 3 6 4 8 9 7
输出
1 3 4 8 9
示例2
输入
5
1 2 8 6 4
输出
1 2 4
说明
其最长递增子序列有3个，（1，2，8）、（1，2，6）、（1，2，4）其中第三个字典序最小，故答案为（1，2，4）
"""

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]

tmp = 1
for i in range(1, n):
    dp[i] = tmp
    for j in range(i, -1, -1):
        if dp[j] + 1 < tmp:
            break
        if arr[i] > arr[j]:
            tmp = max(tmp, dp[j]+1)
            dp[i] = tmp
            if dp[j]+1 > tmp:
                break
max_dp = max(dp)

# for dp_v in range(max_dp, 0, -1):
#     min_v = 99999999
#     for i in range(index, -1, -1):
#         if dp[i] == dp_v and arr[i] < min_v:
#             min_v = arr[i]
#         if dp[i] < dp_v:
#             index = i
#             break
#     res[dp_v-1] = min_v

"""
        int[] res = new int[len];
        int index = res.length - 1;
        int next = Integer.MAX_VALUE;
        for (int k = nums.length - 1; k >= 0; k--){
            if (nums[k] <= next && dp[k] == index + 1){//满足该条件求得的序列就是目标LIS。假设已知LIS最后一个数字（其实就是minTail中最后一个非0值
                //通过该判断求LIS前一个数值？（首先该条件为nums[k]是LIS倒数第二个数值的充分条件，但还需证明由该条件得到的LIS按字典排序最小）。假设除了k满足该条件，
                //还有i，j...满足，那么i，j...不可能在k之后（因为倒着遍历nums），所以推出num[i,j,...]必然大于nums[k]。绝不可能小于或者等于，否则可以推出dp[k]==index+2
                res[index] = nums[k];
                next = res[index];
                index--;
            }
        }
"""
res = [0 for i in range(max_dp)]
index = max_dp - 1
next = 99999999
for k in range(n-1, -1, -1):
    if arr[k] <= next and dp[k] == index+1:
        res[index] = arr[k]
        next = res[index]
        index -= 1

for x in res:
    print(x, end=' ')

n = int(input())
res = []
lines=[]
for i in range(n):
    lines.append(str(input()))
for i in range(n):
    line = [int(x) for x in lines[i]]
    length = len(line)
    flag = [True]
    count = [0]
    dp = [999999]*length
    for i in range(n):
        if line[i] == 1:
            break
        dp[i]=0
    for i in range(n):
        if line[i] == 0:
            continue
        if i-1 >=0 and line[i] == 1 and line[i-1] == 1:

            count[0] = count[0]+1
            dp[i] = dp[i-2] + 1
            line[i-1] = 0
            line[i]=0
            if i+1<n:
                line[i+1] = 1-line[i+1]
        # else:
        #     flag[0] = False
    print(line)
    if sum(line)==0:
        res.append(count[0])
    else:
        res.append('NO')
for x in res:
    print(x)






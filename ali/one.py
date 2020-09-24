n = int(input())
res = []
lines=[]
for i in range(n):
    lines.append(str(input()))
for i in range(n):
    line = [int(x) for x in lines[i]]
    length = len(line)
    flag = [False]
    count = [0]
    def search(new_line, num):
        if sum(new_line)==0:
            flag[0] = True
            count[0] += 1
            return
        for i in range(num, length):
            tmp = new_line.copy()
            tmp[num] = 1-tmp[num]
            if num > 0:
                tmp[num-1]=1-tmp[num-1]
            if num+1 < length:
                tmp[num+1]=1+tmp[num+1]
            search(tmp, num+1)
    for i in range(length):
        search(line,i)
    if flag[0]:
        res.append(count[0])
    else:
        res.append('NO')
for x in res:
    print(x)






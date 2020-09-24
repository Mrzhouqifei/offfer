t = int(input())
def huiwen(s):
    dicts = dict()
    for x in s:
        if x in dicts.keys():
            dicts[x] += 1
        else:
            dicts[x] = 1
    odd_num = 0
    for x in dicts.keys():
        if dicts[x] % 2 == 1:
            odd_num += 1
    return odd_num, dicts

def boyi(s, dicts):
    for i in range(len(s)):
        tmp = s[:i]+s[i+1:]
        odd_num, dicts =huiwen(tmp)
        if odd_num > 1:
            return tmp
    s = s[1:]
    return s

for _ in range(t):
    s = str(input())
    who = 0
    while True:
        odd_num, dicts = huiwen(s)
        if odd_num <= 1:
            break
        s = boyi(s, dicts)
        who = 1 - who
    if who == 0:
        print('Cassidy')
    else:
        print('Eleanore')





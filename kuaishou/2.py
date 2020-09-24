r, n = list(map(int, input().split()))
nums = []
i = 0
while True:
    t = pow(n, i)
    if t > r:
        break
    nums.append(t)
    i+=1
res = []
def dfs(num_now, r, now):
    if now == r:
        res.extend(num_now)
        return True
    elif now > r:
        return False

    for x in nums:
        if x not in num_now:
            tmp = now + x
            num_now.append(x)
            if dfs(num_now, r, tmp):
                return True
            num_now.pop()
now_list =  []
for x in nums:
    now_list.append(x)
    dfs(now_list, r, x)
    now_list.pop()

r = []
for i in range(len(nums)):
    if len(res) > 0:
        if nums[i] == res[0]:
            r.append(i)
            res.pop(0)
print(str(r))
# if len(r) > 0:
#     print(r)
# else:
#     print('')
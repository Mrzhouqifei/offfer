s = str(input().split())
match, left, right = 0, 0 , 0
stack = []
for x in s:
    if x == '(' or x == ')':
        stack.append(x)

while len(stack) > 0:
    t = stack.pop()
    if t == '(':
        if right > 0:
            match += 1
            right -= 1
        else:
            left += 1
    elif t == ')':
        right += 1
print(match, end=' ')
print(left, end=' ')
print(right)






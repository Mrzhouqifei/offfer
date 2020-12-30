
key_value = {}
key_value[2] = 12
key_value[1] = 56
key_value[3] = 1
# 字典按键排序
a = sorted(key_value)
b = sorted(key_value.items(), key=lambda kv:(kv[0], kv[1]))
# 字典按值排序
c = sorted(key_value.items(), key=lambda kv:(kv[1], kv[0]))

print(key_value, a, b, c)


lists = [2,3,4]
print(lists[::-1])
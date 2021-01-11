
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


"""
面试题 10.02. 变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        word_map = defaultdict(list)

        for x in strs:
            word_map[''.join(sorted(x))].append(x)
        return list(word_map.values())